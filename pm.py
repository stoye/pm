import argparse

# Setup the argument parser
pm_parser = argparse.ArgumentParser(description='A Simple Command-Line Project Manager')
pm_subparsers = pm_parser.add_subparsers()

# pm add
pm_add_parser = pm_subparsers.add_parser('add', help='add the current directory as a project')
pm_add_parser.add_argument('project')

# pm list
pm_list_parser = pm_subparsers.add_parser('list', help='list all tracked projects')

# pm remove
pm_remove_parser = pm_subparsers.add_parser('remove', help='remove a project')
pm_remove_parser.add_argument('project')

# pm go
pm_go_parser = pm_subparsers.add_parser('go', help='switch to the given project')
pm_go_parser.add_argument('project')

# pm config
pm_config_parser = pm_subparsers.add_parser('config', help='edit the global configs for pm')
pm_config_subparsers = pm_config_parser.add_subparsers()

pm_add_config_parser = pm_config_subparsers.add_parser('add', help='add a config item to the global config')

pm_get_config_parser = pm_config_subparsers.add_parser('get', help="get a config item's value")

pm_remove_config_parser = pm_config_subparsers.add_parser('remove', help='remove a config item from the global config')

# pm config-project
pm_proj_config_parser = pm_subparsers.add_parser('config-project', help='edit the config for a given project')
pm_proj_config_parser.add_argument('project')
pm_proj_config_subparsers = pm_proj_config_parser.add_subparsers()

pm_add_proj_config_parser = pm_proj_config_subparsers.add_parser('add', help="add a config item to the given project's config")

# Parse the arguments
args = pm_parser.parse_args()
print(args)
