#!/usr/bin/python

import sys
from ansible.module_utils.basic import AnsibleModule

def run_container(container_name, container_image):
    print("Created container: " + container_name + " using image" + container_image)
    print("Container " + container_name + " is running!")

def main():
    module_args = dict(
        container_name=dict(type='str', required=True),
        container_image=dict(type='str', required=True),
        state=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    container_name = module.params['container_name']
    container_image = module.params['container_image']
    state = module.params['state']

    if state == 'running':
        run_container(container_name, container_image)
        ret = "finished"

    if state == 'present':
        create_container(container_name, container_image)
    if state == 'absent':
        delete_container(container_name)
    if state == 'stopped':
        stop_container(container_name)
    if state == 'image_present':
        download_image(container_image)
    if state == 'image_absent':
        delete_image(container_image)
        
    module.exit_json(changed=False, meta=ret)



if __name__ == '__main__':
    main()