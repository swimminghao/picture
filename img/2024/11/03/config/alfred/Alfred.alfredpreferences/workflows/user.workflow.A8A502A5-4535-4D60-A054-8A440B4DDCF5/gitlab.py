# encoding: utf-8
import sys
import argparse
from workflow import Workflow3, ICON_WEB, ICON_WARNING, ICON_INFO, web, PasswordNotFound
from workflow.background import run_in_background, is_running

__version__ = '1.2.1'

log = None

def search_for_project(project):
    """Generate a string search key for a project"""
    elements = []
    elements.append(project['name'])
    elements.append(project['namespace']['path'])
    return u' '.join(elements)

def main(wf):
    # build argument parser to parse script args and collect their
    # values
    parser = argparse.ArgumentParser()
    # add an optional (nargs='?') --setkey argument and save its
    # value to 'apikey' (dest). This will be called from a separate "Run Script"
    # action with the API key
    parser.add_argument('--setkey', dest='apikey', nargs='?', default=None)
    parser.add_argument('--seturl', dest='apiurl', nargs='?', default=None)
    parser.add_argument('query', nargs='?', default=None)
    # parse the script's arguments
    args = parser.parse_args(wf.args)

    ####################################################################
    # Save the provided API key or URL
    ####################################################################

    # decide what to do based on arguments
    if args.apikey:  # Script was passed an API key
        log.info("Setting API Key")
        wf.save_password('gitlab_api_key', args.apikey)
        return 0  # 0 means script exited cleanly

    if args.apiurl:
        log.info("Setting API URL to {url}".format(url=args.apiurl))
        wf.settings['api_url'] = args.apiurl
        return 0

    ####################################################################
    # Check that we have an API key saved
    ####################################################################

    try:
        wf.get_password('gitlab_api_key')
    except PasswordNotFound:  # API key has not yet been set
        wf.add_item('No API key set.',
                    'Please use glsetkey to set your GitLab API key.',
                    valid=False,
                    icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    ####################################################################
    # View/filter GitLab Projects
    ####################################################################

    query = args.query

    projects = wf.cached_data('projects', None, max_age=0)

    if wf.update_available:
        # Add a notification to top of Script Filter results
        wf.add_item('New version available',
                    'Action this item to install the update',
                    autocomplete='workflow:update',
                    icon=ICON_INFO)

    # Start update script if cached data is too old (or doesn't exist)
    if not wf.cached_data_fresh('projects', max_age=3600):
        cmd = ['/usr/bin/python', wf.workflowfile('update.py')]
        run_in_background('update', cmd)

    # Notify the user if the cache is being updated
    if is_running('update'):
        wf.rerun = 1
        wf.add_item('Updating project list via GitLab...',
                    valid=False,
                    icon=ICON_INFO)

    # If script was passed a query, use it to filter projects
    if query and projects:
        projects = wf.filter(query, projects, key=search_for_project, min_score=20)

    if not projects:  # we have no data to show, so show a warning and stop
        wf.add_item('No projects found', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for project in projects:
        wf.add_item(title=project['name_with_namespace'],
                    subtitle=project['path_with_namespace'],
                    arg=project['web_url'],
                    valid=True,
                    icon=None)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3(update_settings={
        'github_slug': 'lukewaite/alfred-gitlab',
        'version': __version__,
        'frequency': 1
    })
    log = wf.logger
    sys.exit(wf.run(main))