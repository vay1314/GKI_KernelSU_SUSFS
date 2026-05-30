#!/usr/bin/env python3
import os
from pathlib import Path

# Runner/本地主目录
RUNNER_HOME = Path(os.environ.get("RUNNER_HOME", str(Path.home())))

# 工作目录
GKI_WORKSPACE = Path(os.environ.get("GKI_WORKSPACE", "/tmp/gki-build"))

# 仓库目录
REPOS_DIR = GKI_WORKSPACE / "repos"

# 内核源码目录
KERNEL_DIR = GKI_WORKSPACE / "kernel"

# 工具链目录
TOOLCHAIN_DIR = GKI_WORKSPACE / "toolchain"
MKBOOTIMG_DIR = GKI_WORKSPACE / "mkbootimg"
REPO_TOOL_DIR = GKI_WORKSPACE / "git-repo"

# 仓库路径
SUSFS_REPO_DIR = REPOS_DIR / "susfs4ksu"
SUKISU_PATCH_REPO_DIR = REPOS_DIR / "SukiSU_patch"
ANYKERNEL_REPO_DIR = REPOS_DIR / "AnyKernel3"
KERNEL_PATCHES_REPO_DIR = REPOS_DIR / "kernel_patches"

# 构建产物目录
ARTIFACTS_DIR = GKI_WORKSPACE / "artifacts"
BOOTIMGS_DIR = GKI_WORKSPACE / "bootimgs"
CACHE_DIR = GKI_WORKSPACE / "cache"

# 缓存目录
CCACHE_DIR = RUNNER_HOME / ".ccache"
BAZEL_CACHE_DIR = RUNNER_HOME / ".cache" / "bazel"

# GitHub 相关
GITHUB_WORKSPACE = Path(os.environ.get("GITHUB_WORKSPACE", "/home/runner/work"))
GITHUB_OUTPUT = os.environ.get("GITHUB_OUTPUT", "")

# 工作流脚本目录
SCRIPTS_DIR = Path(__file__).parent
CONFIG_DIR = SCRIPTS_DIR.parent / "config"
MATRIX_FILE = CONFIG_DIR / "matrix.json"
