/**
 * @file agent_context.h
 * @brief Agent Context Definition
 * @version 0.1
 * @date 2025-07-20
 *
 * @copyright Copyright (c) 2025 Edge AI, LLC. All rights reserved.
 *
 */
#pragma once

#include <agents-cpp/coroutine_utils.h>
#include <agents-cpp/llm_interface.h>
#include <agents-cpp/memory.h>
#include <agents-cpp/tool.h>
#include <agents-cpp/types.h>
#include <map>
#include <memory>
#include <vector>

/**
 * @brief Framework Namespace
 *
 */
namespace agents {

/**
 * @brief Context for an agent, containing tools, LLM, and memory
 */
class AgentContext {
public:
    /**
     * @brief Default constructor for AgentContext
     *
     */
    AgentContext();

    /**
     * @brief Default destructor for AgentContext
     */
    ~AgentContext() = default;

    /**
     * @brief Set the LLM to use
     * @param llm The LLM to use
     */
    void setLLM(std::shared_ptr<LLMInterface> llm);

    /**
     * @brief Get the LLM
     * @return The LLM
     */
    std::shared_ptr<LLMInterface> getLLM() const;

    /**
     * @brief Set the system prompt
     * @param system_prompt The system prompt to use
     */
    void setSystemPrompt(const String& system_prompt);

    /**
     * @brief Get the system prompt
     * @return The system prompt
     */
    const String& getSystemPrompt() const;

    /**
     * @brief Register a tool
     * @param tool The tool to register
     */
    void registerTool(std::shared_ptr<Tool> tool);

    /**
     * @brief Get a tool by name
     * @param name The name of the tool to get
     * @return Pointer to tool
     */
    std::shared_ptr<Tool> getTool(const String& name) const;

    /**
     * @brief Get all tools
     * @return The tools
     */
    std::vector<std::shared_ptr<Tool>> getTools() const;

    /**
     * @brief Execute a tool by name using coroutines
     * @param name The name of the tool to execute
     * @param params The parameters to pass to the tool
     * @return The result of the tool execution
     */
    Task<ToolResult> executeTool(const String& name, const JsonObject& params);

    /**
     * @brief Get the memory
     * @return The memory
     */
    std::shared_ptr<Memory> getMemory() const;

    /**
     * @brief Add a message to the conversation history
     * @param message The message to add
     */
    void addMessage(const Message& message);

    /**
     * @brief Get all messages in the conversation history
     * @return The messages
     */
    std::vector<Message> getMessages() const;

    /**
     * @brief Run a chat completion with the current context using coroutines
     * @param user_message The user message to send
     * @return The LLM response
     */
    Task<LLMResponse> chat(const String& user_message);

    /**
     * @brief Run a chat completion with tools using coroutines
     * @param user_message The user message to send
     * @return The LLM response
     */
    Task<LLMResponse> chatWithTools(const String& user_message);

    /**
     * @brief Stream chat results with AsyncGenerator
     * @param user_message The user message to send
     * @return The LLM response
     */
    AsyncGenerator<String> streamChat(const String& user_message);

    /**
     * @brief Unified multimodal chat (accepts one or more media URIs or data strings)
     * @param user_message The user message to send to the LLM
     * @param uris_or_data The URIs or data to use
     * @return The LLM response
     */
    Task<LLMResponse> chatMultiModal(const String& user_message, const std::vector<String>& uris_or_data);

    /**
     * @brief Unified multimodal streaming chat (accepts one or more media URIs or data strings)
     * @param user_message The user message to send to the LLM
     * @param uris_or_data The URIs or data to use
     * @return The LLM response
     */
    AsyncGenerator<String> streamChatMultiModal(const String user_message, const std::vector<String> uris_or_data);

private:
    /**
     * @brief The LLM to use
     */
    std::shared_ptr<LLMInterface> llm_;

    /**
     * @brief The memory to use
     */
    std::shared_ptr<Memory> memory_;

    /**
     * @brief The tools to use
     */
    std::map<String, std::shared_ptr<Tool>> tools_;

    /**
     * @brief The system prompt to use
     */
    String system_prompt_;

    /**
     * @brief Build messages from multimodal parts
     * @param prompt The prompt to send to the LLM
     * @param uris_or_data The URIs or data to use
     * @return The messages
     */
    std::vector<Message> buildMultimodalParts(const String& prompt, const std::vector<String>& uris_or_data);
};

} // namespace agents