def run_broken(test, device):
    if test.case_name == 'new_nothrow_replace.pass' and device.version < 18:
        return f'android-{device.version}', 'http://b/2643900'
    return None, None
