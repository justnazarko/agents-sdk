/**
 * @example evaluator_optimizer_example.cpp
 * @brief Evaluator Optimizer Example
 * @version 0.1
 * @date 2025-07-20
 *
 * @copyright Copyright (c) 2025 Edge AI, LLC. All rights reserved.
 *
 */
#include <agents-cpp/config_loader.h>
#include <agents-cpp/workflows/evaluator_workflow.h>

#include <iostream>

using namespace agents;

int main(int argc, char* argv[]) {
    // Get API key from .env, environment, or command line
    String api_key;
    auto& config = ConfigLoader::getInstance();

    // Try to get API key from config or environment
    api_key = config.get("GEMINI_API_KEY", "");

    // If not found, check command line
    if (api_key.empty() && argc > 1) {
        api_key = argv[1];
    }

    // Still not found, show error and exit
    if (api_key.empty()) {
        std::cout << ("API key not found. Please:") << std::endl;
        std::cout << ("1. Create a .env file with GEMINI_API_KEY=your_key, or") << std::endl;
        std::cout << ("2. Set the GEMINI_API_KEY environment variable, or") << std::endl;
        std::cout << ("3. Provide an API key as a command line argument") << std::endl;
        return EXIT_FAILURE;
    }

    // Create LLM
    auto llm = createLLM("google", api_key, "gemini-1.5-flash");

    // Configure LLM options
    LLMOptions options;
    options.temperature = 0.4;
    options.max_tokens = 2048;
    llm->setOptions(options);

    // Create agent context
    auto context = std::make_shared<AgentContext>();
    context->setLLM(llm);

    // Create evaluator-optimizer workflow
    workflows::EvaluatorWorkflow workflow(context);

    // Set optimizer prompt
    workflow.setOptimizerPrompt(
        "You are an optimizer assistant that produces high-quality responses to user queries. "
        "Your task is to generate the best possible response to the user's query. "
        "If you receive feedback, use it to improve your response."
    );

    // Set evaluator prompt
    workflow.setEvaluatorPrompt(
        "You are an evaluator assistant that critically assesses the quality of responses. "
        "Your task is to provide honest, detailed feedback on the response to help improve it. "
        "Focus on specific areas where the response could be enhanced."
    );

    // Set evaluation criteria
    workflow.setEvaluationCriteria({
        "Accuracy: Is the information provided accurate and factually correct?",
        "Completeness: Does the response address all aspects of the query?",
        "Clarity: Is the response clear, well-organized, and easy to understand?",
        "Relevance: Is the response directly relevant to the query?",
        "Actionability: Does the response provide practical, actionable information where appropriate?"
    });

    // Set maximum iterations
    workflow.setMaxIterations(3);

    // Set minimum acceptable score
    workflow.setMinimumAcceptableScore(0.85);

    // Set custom evaluator and optimizer functions (optional)
    workflow.setEvaluator([](const String& input, const String& output) -> JsonObject {
        // This is a custom evaluator function that would normally implement
        // specialized evaluation logic, but here we'll let the default LLM-based
        // evaluator do the work by returning an empty result
        (void)input;
        (void)output;
        return JsonObject();
    });

    workflow.setOptimizer([](const String& input, const JsonObject& feedback) -> String {
        // This is a custom optimizer function that would normally implement
        // specialized optimization logic, but here we'll let the default LLM-based
        // optimizer do the work by returning an empty string
        (void)input;
        (void)feedback;
        return "";
    });

    // Process user inputs until exit
    std::cout << "Enter queries (or 'exit' to quit):" << std::endl;
    String user_input;
    while (true) {
        std::cout << "> ";
        std::getline(std::cin, user_input);

        if (user_input == "exit" || user_input == "quit" || user_input == "q") {
            break;
        }

        if (user_input.empty()) {
            continue;
        }

        try {
            std::cout << "Starting evaluator-optimizer workflow..." << std::endl;

            // Run the workflow
            JsonObject result = workflow.run(user_input);

            // Display the final result
            std::cout << "\nFinal Response:" << std::endl;
            std::cout << result["final_response"].get<String>() << std::endl;

            // Display evaluation information
            std::cout << "\nEvaluation Information:" << std::endl;
            std::cout << "Iterations: " << result["iterations"].get<int>() << std::endl;
            std::cout << "Final Score: " << result["final_score"].get<double>() << std::endl;

            if (result.contains("evaluations")) {
                std::cout << "\nEvaluation History:" << std::endl;
                for (const auto& eval : result["evaluations"]) {
                    std::cout << "Iteration " << eval["iteration"].get<int>() << ": Score = "
                              << eval["score"].get<double>() << std::endl;
                    std::cout << "Feedback: " << eval["feedback"].get<String>() << std::endl;
                    std::cout << "----------" << std::endl;
                }
            }

            std::cout << "--------------------------------------" << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }

    return EXIT_SUCCESS;
}