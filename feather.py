#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

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
    container_image = module.params['container_image ']

    try:
   

    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()