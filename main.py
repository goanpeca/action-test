import os
from github import Github, Auth
from subprocess import check_output


# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()    


def sync_website_content(source_repo, source_folder, source_ref, translations_repo, translations_folder, translations_ref):
    # p = Popen("rsync -av --delete pandas/web/pandas/ pandas-translations/content/en/"
    # cd pandas-translations
    # git checkout -b ${{ env.BRANCH_NAME }}
    cmds = ['git', 'clone', f'https://github.com/{source_repo}.git']
    if source_folder:
        cmds.append(source_folder)
    out = check_output(cmds)
    print(out)

    cmds = ['git', 'clone', f'https://github.com/{translations_repo}.git']
    if translations_folder:
        cmds.append(translations_folder)
    out = check_output(cmds)

    out = check_output(['git', 'config', '--global', 'user.email', '"actions@github.com"'])
    print(out)

    out = check_output(['git', 'config', '--global', 'user.name', '"GitHub Actions"'])
    print(out)

    out = check_output(['ls'])
    print(out)

    # git add .
    # # Only proceed to commit if there are changes
    # if git diff --staged --quiet; then
    # echo "No changes to commit."
    # echo "CONTENT_CHANGED=false" >> $GITHUB_ENV
    # else
    # git commit -m "Update website content"
    # echo "CONTENT_CHANGED=true" >> $GITHUB_ENV
    # git push -u origin ${{ env.BRANCH_NAME }}
    # fi



def main():
    github_token = os.environ["GITHUB_TOKEN"]
    source_repo = os.environ["INPUT_SOURCE_REPO"]
    source_folder = os.environ["INPUT_SOURCE_FOLDER"]
    source_ref = os.environ["INPUT_SOURCE_REF"]
    translations_repo = os.environ["INPUT_TRANSLATIONS_REPO"]
    translations_folder = os.environ["INPUT_TRANSLATIONS_FOLDER"]
    translations_ref = os.environ["INPUT_TRANSLATIONS_REF"]

    # repository = os.environ["GITHUB_REPOSITORY"]

    auth = Auth.Token(github_token)
    g = Github(auth=auth)

    repository = "Scientific-Python-Translations/pandas-translations"
    repo = g.get_repo(translations_repo)
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
        print(pr.number, pr.title)
        if pr.title == "Update website content":
            break
    
    sync_website_content(source_repo, source_folder, source_ref, translations_repo, translations_folder, translations_ref)

    g.close()

    set_github_action_output('todo', 'Hello world')
    print("TESTING")


if __name__ == "__main__":
    main()
