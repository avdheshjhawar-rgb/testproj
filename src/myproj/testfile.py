import argparse
from clearml import Task

if __name__ == "__main__":
    print("are we local???", Task.running_locally())
    task = Task.init(project_name="Project0061", task_name="testfile-git-repo", reuse_last_task_id=False)
    # p = argparse.ArgumentParser()
    # p.add_argument("config", type=argparse.FileType("r"))
    # args = p.parse_args()
    # print("got config", args.config)
    task.execute_remotely(queue_name="avdhesh")