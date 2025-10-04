/**
 * @file media_envelope.h
 * @brief Minimal helpers for a canonical media JSONObject envelope used across tools and providers
 * @version 0.1
 * @date 2025-09-17
 *
 * The canonical envelope shape (all fields optional unless stated):
 * {
 *   "type": "text" | "image" | "audio" | "video",                    // required
 *   "text": "...",                                                   // when type==text
 *   "mime": "image/png" | "audio/wav" | "video/mp4",                 // required for non-text
 *   "uri":  "http(s)://..." | "file://..." | "data:...",             // exactly one of uri or data
 *   "data": "<base64-bytes>",                                        // exactly one of uri or data
 *   "meta": {                                                        // optional metadata
 *     "width": 1024, "height": 768, "fps": 30.0, "duration_s": 3.2,
 *     "sample_rate_hz": 16000, "channels": 1
 *   }
 * }
 *
 * Compatibility: also accepts {"type":"image_url", "image_url":{"url":"..."}}
 */

#pragma once

#include <agents-cpp/types.h>

namespace agents {

/**
 * @brief Media envelope namespace
 */
namespace media {

/**
 * @brief Quick probe to see if JSONObject looks like a media envelope (canonical or compatible)
 */
bool isMediaPart(const JsonObject& j);

/**
 * @brief Normalize various accepted shapes into the canonical envelope, validating constraints
 * @throws std::invalid_argument if the input cannot be normalized to a valid envelope
 */
JsonObject normalizeMediaPart(JsonObject j);

/**
 * @brief Extract MIME type (returns empty string if not present)
 */
String getMime(const JsonObject& j);

/**
 * @brief Returns true if the envelope carries a URI reference
 */
bool hasUri(const JsonObject& j);

/**
 * @brief Returns true if the envelope carries inline base64 data
 */
bool hasData(const JsonObject& j);

/**
 * @brief Best-effort parse of a Data URL to extract MIME type (empty if not parsable)
 */
String mimeFromDataUrl(const String& data_url);

/**
 * @brief Parse a string into a media envelope if possible; returns nullopt if not media
 */
std::optional<JsonObject> tryParseEnvelopeFromString(const String& content);

/** Media envelope builders **/

/**
 * @brief Create a text media envelope
 * @param s The text content
 * @return The media envelope
 */
inline JsonObject text(const String& s) {
    return JsonObject{{"type","text"},{"text",s}};
}

/**
 * @brief Create an image media envelope
 * @param uri The image URI
 * @param mime The image MIME type
 * @param meta The image metadata
 * @return The media envelope
 */
inline JsonObject imageUri(const String& uri, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","image"},{"mime",mime},{"uri",uri}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

/**
 * @brief Create an image media envelope with base64 data
 * @param base64 The base64 data
 * @param mime The image MIME type
 * @param meta The image metadata
 * @return The media envelope
 */
inline JsonObject imageData(const String& base64, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","image"},{"mime",mime},{"data",base64}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

/**
 * @brief Create an audio media envelope
 * @param uri The audio URI
 * @param mime The audio MIME type
 * @param meta The audio metadata
 * @return The media envelope
 */
inline JsonObject audioUri(const String& uri, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","audio"},{"mime",mime},{"uri",uri}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

/**
 * @brief Create an audio media envelope with base64 data
 * @param base64 The base64 data
 * @param mime The audio MIME type
 * @param meta The audio metadata
 * @return The media envelope
 */
inline JsonObject audioData(const String& base64, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","audio"},{"mime",mime},{"data",base64}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

/**
 * @brief Create a video media envelope
 * @param uri The video URI
 * @param mime The video MIME type
 * @param meta The video metadata
 * @return The media envelope
 */
inline JsonObject videoUri(const String& uri, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","video"},{"mime",mime},{"uri",uri}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

/**
 * @brief Create a video media envelope with base64 data
 * @param base64 The base64 data
 * @param mime The video MIME type
 * @param meta The video metadata
 * @return The media envelope
 */
inline JsonObject videoData(const String& base64, const String& mime, JsonObject meta = {}) {
    JsonObject j{{"type","video"},{"mime",mime},{"data",base64}};
    if (!meta.empty()) j["meta"] = std::move(meta);
    return j;
}

} // namespace media
} // namespace agents


