import os
import sys

def check_sig_info(sig, access_token):
    print('\nStarting to check sig info of sig {}'.format(sig))
    return 1

if __name__ == '__main__':
    # diff_files = [{'from': 'sig/Compiler/committers.md', 'to': 'sig/Compiler/committers.md'},
    #               {'from': 'sig/Compiler/sig-info.yaml', 'to': 'sig/Compiler/sig-info.yaml'}]
    # diff_files = check_diff_files()
    # print(diff_files)
    # change_sigs = []
    # for diff_file in diff_files:
    #     from_file = diff_file['from']
    #     to_file = diff_file['to']
    #     if len(from_file) > 2 and from_file.split('/')[0] == 'sig':
    #         change_sigs.append(from_file.split('/')[1])
    #     if len(to_file) > 2 and to_file.split('/')[0] == 'sig':
    #         change_sigs.append(to_file.split('/')[1])
    # print(change_sigs)
    # change_sigs = sorted(list(set(change_sigs)))
    # print(change_sigs) # ['sig-KIRAN-DESKTOP']
    change_sigs = ['sig-KIRAN-DESKTOP']
    # owners_file_path = os.path.join("community", 'sig', 'Compiler', 'OWNERS')
    # print(owners_file_path)
    errors = 0
    for change_sig in change_sigs:
        if change_sig == 'sig-template':
            print('The SIG sig-template is used only as an example, skip the check.')
            continue
        if os.path.exists(os.path.join("community", 'sig', change_sig, 'OWNERS')):
            print('WARNING! sig {} has OWNERS file yet, found {} warnings'.format(change_sig, errors))
            continue
        errors += check_sig_info(change_sig, '124124')

    if errors != 0:
        print('\nCheck sig info failed: Find {} errors.'.format(errors))
        sys.exit(1)
    print('\nCheck sig info: PASS :)')
