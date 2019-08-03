# Vim

Vim has two modes:

1. Insert mode (Where you can just type like normal text editor. Press i for insert mode)
2. Command mode (Where you give commands to the editor to get things done. Press ESC for command mode)

## Insert mode

Task                              | Command
----------------------------------|--------------------------------
Append text at the end            | `a`

## Navigating

Task                              | Command
----------------------------------|--------------------------------

## Editing

Task                              | Command
----------------------------------|--------------------------------
Delete a character                | `x`
Undo the last command             | `u` 
Redo the last command             | `CTRL + r`
Save and exit                     | `wq`
Trash all changes                 | `:q!`
Quit all                          | `qa`
Cut line                          | `dd`
Copy                              |
Paste                             |

## Tabs

Task                                 | Command
-------------------------------------|--------------------------------
Open multiple files in separate tabs | `vim -p /path/to/file1 /path/file2 file3`
Jump to the next tab                 | `gt` or `:tabn[ext]`
Jump to the previous tab             | `gT` or `:tabp[revious]`
Jump to a specific tab               | `ngt` where n is the tab index starting at 1
Close the current tab                | `:tabc[lose]`

## References

- https://devhints.io/vim
- https://blog.confirm.ch/mastering-vim-working-with-multiple-files
- https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started
