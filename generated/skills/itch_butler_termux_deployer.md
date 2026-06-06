# itch-butler-termux-deployer Skill

This is the Thunder Brainstorm doc-viewer mirror of the installed Codex skill:

```text
/data/data/com.termux/files/home/.codex/skills/itch-butler-termux-deployer/SKILL.md
```

The installed skill remains the source of truth for Codex discovery. This generated copy exists so the workflow is visible in the Thunder Brainstorm doc viewer.

## Installed Skill

---
name: itch-butler-termux-deployer
description: >-
  Use when Codex needs to upload an itch.io build with butler from the user's Android/Termux workspace, especially HTML/canvas web builds from GodotProjects. Covers checking ITCH_API_KEY/BUTLER_API_KEY without exposing secrets, building butler from official itchio/butler source when the official Linux ARM64 binary cannot run under Android, pushing hidden release-candidate builds, checking channel status, and documenting upload IDs.
---

# Itch Butler Termux Deployer

## Core Rules

- Use butler for build uploads only. Itch project page metadata, cover images, screenshots, and HTML playable settings are normally managed in the itch web UI.
- Do not print, write, package, or commit API keys. Map `ITCH_API_KEY` to `BUTLER_API_KEY` only inside the upload command when needed.
- Ask before installing missing system tools such as `golang`.
- Prefer hidden/private release-candidate uploads first.

## Preflight

1. Confirm the itch project already exists. Butler cannot create the project page. The target should look like:

```text
username/game:channel
```

Example:

```text
grailawakeninggames/marrow-runner:html
```

2. Validate the build zip before upload:

```sh
python3 - <<'PY'
import zipfile
with zipfile.ZipFile('release/<build>.zip') as z:
    print('bad', z.testzip(), 'entries', len(z.namelist()))
PY
```

3. Confirm key presence without exposing it:

```sh
sh -lc '. ~/.bashrc >/dev/null 2>&1; if [ -n "$BUTLER_API_KEY" ] || [ -n "$ITCH_API_KEY" ]; then echo itch-key=set; else echo itch-key=missing; fi'
```

## Butler On Termux / Android

The official Linux ARM64 butler binary may download successfully but fail under Termux because it expects the GNU/Linux loader, not Android's linker. A typical failure is:

```text
unexpected e_type: 2
```

If this happens, build butler locally from official source after getting permission to install Go:

```sh
pkg install -y golang git
build_dir=/data/data/com.termux/files/usr/tmp/butler-src-$(date +%s)
git clone --depth 1 https://github.com/itchio/butler.git "$build_dir"
mkdir -p /data/data/com.termux/files/usr/tmp/butler-android-bin
cd "$build_dir"
CGO_ENABLED=1 go build -o /data/data/com.termux/files/usr/tmp/butler-android-bin/butler .
/data/data/com.termux/files/usr/tmp/butler-android-bin/butler version
```

A locally built Android binary may report `head, no build date`; that is acceptable if `butler version`, `butler push`, and `butler status` work. Its self-version check may print a 404 for `android-arm64-head`; that is also acceptable if the command continues.

## Upload

Use `BUTLER_API_KEY` if set; otherwise map `ITCH_API_KEY` for the single command:

```sh
sh -lc '. ~/.bashrc >/dev/null 2>&1; BUTLER_API_KEY="${BUTLER_API_KEY:-$ITCH_API_KEY}" /data/data/com.termux/files/usr/tmp/butler-android-bin/butler push release/<build>.zip username/game:html --userversion <version> --hidden'
```

After upload, check status:

```sh
sh -lc '. ~/.bashrc >/dev/null 2>&1; BUTLER_API_KEY="${BUTLER_API_KEY:-$ITCH_API_KEY}" /data/data/com.termux/files/usr/tmp/butler-android-bin/butler status username/game:html'
```

Record channel, upload ID, build ID, and version in the final response.

## Post-Upload

Tell the user to verify on itch:

- The HTML build is selected as playable in browser.
- Fullscreen/embed settings are correct.
- Page cover, screenshots, and description are set manually.
- Mobile iframe controls, audio unlock, pause/mute, and exit/menu flow work on the hosted page.

## References

Use `references/termux-android-notes.md` for the exact Android binary issue and expected output patterns.

## Marrow Runner Observed Target

Known Marrow Runner release target:

```text
grailawakeninggames/marrow-runner:html
https://grailawakeninggames.itch.io/marrow-runner
```

User-facing/social URL may be:

```text
https://valarsbeard.itch.io/marrow-runner
```

Latest observed successful channel state:

```text
channel: html
version: v0.9.0-rc3
upload: #17807876
build: #1707945
```

Before reporting external files such as screenshots or cover images as ready for itch upload from Android, refresh Android media indexing for those files so browser/file pickers can see them.



## Observed Local Termux Build

Observed on 2026-06-05 in this Android/Termux workspace:

```text
Go: /data/data/com.termux/files/usr/bin/go
go version: go1.26.4 android/arm64
Butler binary: /data/data/com.termux/files/usr/tmp/butler-android-bin/butler
Butler source checkout: /data/data/com.termux/files/usr/tmp/butler-src-1780609690
butler version: head, no build date
```

The binary was built from official `itchio/butler` source after the official Linux ARM64 binary path proved unsuitable for Termux/Android. The self-version check may print an `android-arm64-head/LATEST` HTTP 404; uploads and status checks can still be valid.
