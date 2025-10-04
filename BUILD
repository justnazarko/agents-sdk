# Main library build recipe

# C++ Requests
cc_import(
    name = "cpr",
    shared_library = select({
        "@platforms//os:macos": "lib/macos/libcpr.1.dylib",
        "@platforms//os:linux": "lib/linux/libcpr.so.1",
        "//conditions:default": None,
    }),
)

# Curl
cc_import(
    name = "curl",
    shared_library = select({
        "@platforms//os:macos": "lib/macos/libcurl.4.dylib",
        "@platforms//os:linux": "lib/linux/libcurl.so.4.11.0",
        "//conditions:default": None,
    }),
)

# Python for python execution tool
cc_import(
    name = "python",
    shared_library = select({
        "@platforms//os:macos": "lib/macos/libpython3.11.dylib",
        "@platforms//os:linux": "lib/linux/libpython3.11.so",
        "//conditions:default": None,
    }),
)

# Main library
cc_import(
    name = "agents_cpp",
    hdrs = glob([
        "include/agents-cpp/**/*.h",
        "include/spdlog/**/*.h"
    ]),
    includes = [
        "include",
    ],
    shared_library = select({
        "@platforms//os:macos": "lib/macos/libagents_cpp_shared_lib.dylib",
        "@platforms//os:linux": "lib/linux/libagents_cpp_shared_lib.so",
        "//conditions:default": None,
    }),
    deps = [
        ":cpr",
        ":curl",
        ":python"
    ],
    visibility = ["//visibility:public"]
)

# End of BUILD file