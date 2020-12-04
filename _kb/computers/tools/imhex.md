---
title: ImHex Editor
---

## Debian Deps

- nlohmann-json3-dev
- libglfw3-dev
- libssl-dev
- libcapstone-dev
- llvm
- libglm-dev


## With Alternate Capstone

1. See [Capstone notes](/computers/tools/capstone) for details about Capstone in alternate paths.
2. Patch: `sed -i 's|capstone/capstone.h|capstone.h|' include/views/view_disassembler.hpp`
3. Patch: `sed -i 's|libLLVMDemangle.so|${LLVM_LIBRARY_DIRS}/libLLVMDemangle.a|' CMakeLists.txt
4. Build with `PKG_CONFIG_PATH=${HOME}/.local/lib/pkgconfig cmake ..`
