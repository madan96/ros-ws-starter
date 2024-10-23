# ROS Workspace Starter

Example repo for starting your ROS workspace.

### Installing the packages

Go to the source directory of your ROS workspace and clone this repository with
```bash
git clone git@github.com:madan96/ros-ws-starter.git
```

Then, initialise all the submodules

```bash
cd ros-ws-starter
git submodule update --init --recursive
```

Finally, remember to source your workspace.

### Adding new packages to the workspace

Add a new package to the workspace repo as a submodule

```
git submodule add <repo-url>
git commit -m "add <package-name>"
git push
```

### Update existing packages

Ideally, the workspace repository should be used once you have a stable version for most packages. If at a later point, you make updates to one of the packages, and would like the commit ID for the submodule to be updated run the following commands:

```
git submodule update --remote --merge
git add <package-name>
git commit -m "update <package-name> to latest commit"
git push
```

### Running ROS tests for the workspace

To run `rostests` that usually involve running multiple nodes (similar to a launch file), run `catkin run_tests`.
