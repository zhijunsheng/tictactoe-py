import os, unittest

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any decendents."""
    total = os.path.getsize(path)                       # account for direct usage
    if os.path.isdir(path):                             # if this is a directory
        for filename in os.listdir(path):               # then for each child:
            childpath = os.path.join(path, filename)    # compose full path to child
            total += disk_usage(childpath)              # add child's usage to total

    print('{0:<7}'.format(total), path)                 # descriptive output (optional)
    return total                                        # return the grand total

class TestFileSystems(unittest.TestCase):

    def test_disk_usage(self):
        usage = disk_usage('/Users/zhijunsheng/dev_learn_py/tictactoe-py/LICENSE')
        self.assertEqual(1063, usage)

if __name__ == '__main__':
    unittest.main()
