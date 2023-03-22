#!/usr/bin/python
""" insert backup name into survey """
# -*- coding: utf-8 -*-

import requests
from ansible.module_utils.basic import AnsibleModule


def main():
    """ vars between ansible and python module """
    fields = {
        "imap_host": {"required": True, "type": 'str'},
        "imap_port": {"required": False, "type": 'str'},
        "imap_username": {"required": True, "type": 'str'},
        "imap_pwd": {"required": True, "type": 'str'},
    }
    module = AnsibleModule(argument_spec=fields)
    awx_admin_token = module.params['awx_admin_token']
    text = module.params['text']
    awx_url = module.params['awx_url']
    survey_field = module.params['survey_field']

    hed = {'Authorization': 'Bearer ' + awx_admin_token}
    # try to connect to ansible API
    try:
        req = requests.get(url=awx_url, headers=hed)
    except requests.exceptions.RequestException as err:
        raise module.fail_json(msg=str(err))
    # if response then check status code
    if req.status_code != 200:
        module.fail_json(msg="Error: can't download survey, "
                             "make sure you are allowed to connect, "
                             "check permissions and survey_id")
    data = req.json()
    # check spec
    try:
        element = [data['spec'], data['spec'][0]['question_name']]
    except KeyError as err:
        raise module.fail_json(msg="Error: this survey is enabled"
                                   " but does not contains any element") from err
    # del element even if no more needed to pass linter
    del element
    found = False
    # search survey_field position in json
    for i in range(0, len(data['spec'])):
        if data['spec'][i]['question_name'] == survey_field:
            # insert text in survey_field
            data['spec'][i]["choices"] += '\n' + text
            found = True
            break
    if not found:
        module.fail_json(msg=f"Error: survey_field '{survey_field}'")
    # post new values
    req = requests.post(url=awx_url, json=data, headers=hed)
    if req.status_code != 200:
        module.fail_json(msg="Error: check token permissions"
                             " to write on target job_template")
    else:
        # everything seems ok
        module.exit_json(changed=False, meta=data)


if __name__ == "__main__":
    main()
