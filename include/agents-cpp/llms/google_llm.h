/**
 * @file google_llm.h
 * @brief Google LLM Definition
 * @version 0.1
 * @date 2025-07-20
 *
 * @copyright Copyright (c) 2025 Edge AI, LLC. All rights reserved.
 *
 */
#pragma once

#include <agents-cpp/llm_interface.h>

namespace agents {
namespace llms {

/**
 * @brief Implementation of LLMInterface for Google Gemini models
 */
class GoogleLLM : public LLMInterface {
public:
    /**
     * @brief Constructor
     * @param api_key The API key
     * @param model The model to use
     */
    GoogleLLM(const String& api_key = "", const String& model = "gemini-1.5-pro");
    /**
     * @brief Destructor
     */
    ~GoogleLLM() override = default;

    /**
     * @brief Get available models from Google
     * @return The available models
     */
    std::vector<String> getAvailableModels() override;

    /**
     * @brief Set the model to use
     * @param model The model to use
     */
    void setModel(const String& model) override;

    /**
     * @brief Get current model
     * @return The current model
     */
    String getModel() const override;

    /**
     * @brief Set API key
     * @param api_key The API key
     */
    void setApiKey(const String& api_key) override;

    /**
     * @brief Set API base URL (for self-hosted or proxied endpoints)
     * @param api_base The API base URL
     */
    void setApiBase(const String& api_base) override;

    /**
     * @brief Set options for API calls
     * @param options The options
     */
    void setOptions(const LLMOptions& options) override;

    /**
     * @brief Get current options
     * @return The current options
     */
    LLMOptions getOptions() const override;

    /**
     * @brief Generate completion from a prompt
     * @param prompt The prompt
     * @return The completion
     */
    LLMResponse chat(const String& prompt) override;

    /**
     * @brief Generate completion from a list of messages
     * @param messages The messages
     * @return The completion
     */
    LLMResponse chat(const std::vector<Message>& messages) override;

    /**
     * @brief Generate completion with available tools
     * @param messages The messages
     * @param tools The tools
     * @return The completion
     */
    LLMResponse chatWithTools(
        const std::vector<Message>& messages,
        const std::vector<std::shared_ptr<Tool>>& tools
    ) override;

    /**
     * @brief Stream results with callback
     * @param messages The messages
     * @param callback The callback
     */
    void streamChat(
        const std::vector<Message>& messages,
        std::function<void(const String&, bool)> callback
    ) override;

    /**
     * @brief Upload a local media file to the provider's file storage and
     *        return a canonical media envelope (e.g., with fileUri).
     * @param local_path Local filesystem path
     * @param mime The MIME type of the media file
     * @param binary Optional binary content of the media file
     * @return Optional envelope; std::nullopt if unsupported
     */
    std::optional<JsonObject> uploadMediaFile(const String& local_path, const String& mime, const String& binary = "") override;

private:
    String api_key_;
    String api_base_ = "https://generativelanguage.googleapis.com/v1";
    String model_;
    LLMOptions options_;

    /**
     * @brief Convert Message list to Google API format
     * @param messages The messages
     * @param tools The tools
     * @return The Google API format
     */
    JsonObject formatMessages(
        const std::vector<Message>& messages, const std::vector<std::shared_ptr<Tool>>& tools);

    /**
     * @brief Convert Google API response to LLMResponse
     * @param response The response
     * @return The LLMResponse
     */
    LLMResponse parseGoogleResponse(const JsonObject& response);

    /**
     * @brief Make API call to Google
     * @param request_body The request body
     * @param stream Whether to stream the response
     * @return The response
     */
    JsonObject makeApiCall(const JsonObject& request_body, bool stream = false);

    /**
     * @brief Get the endpoint URL based on the model
     * @return The endpoint URL
     */
    String getEndpoint() const;

    /**
     * @brief Map media envelope to Google parts array
     * @param env The media envelope
     * @param out_parts The output parts array
     * @return True if the envelope was mapped, false otherwise
     */
    bool mapEnvelopeToGoogle(const JsonObject& env, JsonObject& out_parts);

    /**
     * @brief Start a resumable session
     * @param api_key The API key
     * @param content_length The content length
     * @param mime The MIME type
     * @param display_name The display name
     * @return The resumable session
     */
    String startResumableSession(const String& api_key, int64_t content_length, const String& mime, const String& display_name) const;

    /**
     * @brief Upload bytes to the resumable session
     * @param upload_url The upload URL
     * @param data The data to upload
     * @param content_length The content length
     * @return The response
     */
    JsonObject uploadBytesFinalize(const String& upload_url, const String& data, int64_t content_length) const;
};

} // namespace llms
} // namespace agents