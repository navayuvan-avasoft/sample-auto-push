import subprocess


def execute_command(cmd):
    output = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]
    return output


def checkout_to_main_and_rebase():
    cmd = 'git checkout main && git pull origin main --rebase'
    print(execute_command(cmd))


def checkout_to_dev_and_rebase():
    cmd = 'git checkout dev && git pull origin main -r'
    output = execute_command(cmd)
    if ('CONFLICT (content):' in output):
        return False
    return True


def force_push_to_branch(branch):
    cmd = "git push origin {0} -f".replace("{0}", branch)
    print(execute_command(cmd))


checkout_to_main_and_rebase()
status = checkout_to_dev_and_rebase()
print(status)
if (not status):
    raise ValueError("Aborting the process. Needs Auto Merging.")

force_push_to_branch('dev')
