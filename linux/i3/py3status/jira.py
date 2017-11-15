import subprocess
import os
import sys


class Py3status:
    def on_click(self, json, i3status_config, event):
        """
        clicky clicky
        """

        if event['button'] == 1:
            with open(os.devnull, 'w') as fnull:
                result = subprocess.call(['xdg-open', 'https://jira.zappos.net/secure/Dashboard.jspa'],
                                         stdout=fnull,
                                         stderr=fnull)

    def jira(self, json, i3status_config):
        """
        Get and display count of open tickets in Jira
        """
        response = {'full_text': '', 'name': 'jira', 'color': '#205081'}
        position = 0

        try:
            import requests

            auth = 'bWl3YWxrZXI6ZDBzb21ldGhpbmdhd2Vzb21FIQ=='

            s = requests.Session()
            s.headers.update({'Authorization': 'Basic %s' % auth})

            r = s.get('https://jira.zappos.net/rest/api/2/search?jql=assignee+%3D+miwalker+AND+resolution+%3D+Unresolved', verify=False)

            about = r.json()
            data = about['total']
            response['full_text'] = 'Jira: '
            response['full_text'] += str(data)

        except Exception as e:
            response['full_text'] = 'Jira is broke!'
            response['color'] = '#ff0000'
        finally:
            return (position, response)
