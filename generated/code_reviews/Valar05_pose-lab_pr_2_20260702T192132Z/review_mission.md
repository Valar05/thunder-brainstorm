Review GitHub PR Valar05/pose-lab#2.

Required first steps:
1. Call get_pr_metadata.
2. Call list_pr_files.
3. Call get_pr_diff.
4. Read touched files and relevant call sites/tests/docs with read_file_at_ref and search_repo_at_ref.
5. Use list_ci_checks for the PR head SHA when available.
6. Call finalize_review with strict JSON.

Do not produce prose as the final review. Use finalize_review.
