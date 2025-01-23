import os
from github import Github, Auth

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()    

def main():
    token = os.environ["GITHUB_TOKEN"]
    src = os.environ["INPUT_SOURCE"]
    dest = os.environ["INPUT_DESTINATION"]

    auth = Auth.Token(token)
    g = Github(auth=auth)

    repo = g.get_repo("PyGithub/PyGithub")
    print(repo.name)

    # To close connections after use
    g.close()

    set_github_action_output('todo', 'Hello world')
    print("TESTING")


if __name__ == "__main__":
    main()
