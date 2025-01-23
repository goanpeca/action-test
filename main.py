import os
from github import Github, Auth
from subprocess import check_output
# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()    


def sync_website_content():
    pass
    # p = Popen("rsync -av --delete pandas/web/pandas/ pandas-translations/content/en/"
    # cd pandas-translations
    # git checkout -b ${{ env.BRANCH_NAME }}
    out = check_output(['git', 'clone', 'https://github.com/pandas-dev/pandas.git'])
    print(out)
    out = check_output(['ls'])
    print(out)
    out = check_output(['git', 'config', '--global', 'user.email', '"actions@github.com"'])
    print(out)
    out = check_output(['git', 'config', '--global', 'user.name', '"GitHub Actions"'])
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
    token = os.environ["GITHUB_TOKEN"]
    src = os.environ["INPUT_SOURCE"]
    dest = os.environ["INPUT_DESTINATION"]
    repository = os.environ["GITHUB_REPOSITORY"]

    auth = Auth.Token(token)
    g = Github(auth=auth)

    repo = g.get_repo(repository)
    pulls = repo.get_pulls(state='open', sort='created')
    for pr in pulls:
        print(pr.number, pr.title)

    sync_website_content()

    g.close()

    set_github_action_output('todo', 'Hello world')
    print("TESTING")


if __name__ == "__main__":
    main()
