# android-external-file-refresh Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/android-external-file-refresh/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: android-external-file-refresh
description: "Use when Codex moves, copies, exports, resizes, downloads, or generates files into Android-visible storage such as Pictures, Download, Documents, screenshots, page assets, icons, audio, or other files the user expects to see in Google Files, gallery apps, upload pickers, or share sheets."
---

# Android External File Refresh

Use this whenever a task creates or moves files for external use on Android shared storage.

## Workflow

1. Identify the final external files, usually under `/storage/emulated/0/Pictures`, `/storage/emulated/0/Download`, or `/storage/emulated/0/Documents`.
2. Prefer non-destructive sibling filenames unless the user asked for overwrite.
3. Verify file existence and, for images/audio, basic dimensions/duration when practical.
4. Refresh Android media/file indexing for each final file before reporting completion:
   ```sh
   am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file:///storage/emulated/0/Pictures/path/to/file.png"
   ```
5. If many files were created in one folder, refresh representative files and the parent folder if needed.
6. Report the final paths after refresh.

## Why

Android apps may not immediately see files created from Termux or copied by scripts. Refreshing avoids the user being unable to find a file in Google Files, gallery apps, browser upload controls, or share sheets.

