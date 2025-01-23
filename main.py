import os
from github import Github, Auth

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()    

def main():
    # using an access token
    token = os.environ["GITHUB_TOKEN"]
    auth = Auth.Token(token)

    # Public Web Github
    g = Github(auth=auth)

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)

    # To close connections after use
    g.close()

    src = os.environ["INPUT_SOURCE"]
    dest = os.environ["INPUT_DESTINATION"]

    set_github_action_output('todo', 'Hello world')
    print("TESTING")


if __name__ == "__main__":
    main()
