# Vim

Vim has two modes:

1. Insert mode (Where you can just type like normal text editor. Press i for insert mode)
2. Command mode (Where you give commands to the editor to get things done. Press ESC for command mode)

## Insert mode

Task                                   | Command
---------------------------------------|--------------------------------
Insert text after the cursor           | `a` for Append
Insert text after the end of the line  | `A`
Insert a line below the cursor         | `o` for Open a line
Insert a line above the cursor         | `O`

## Navigating

Task                                            | Command
------------------------------------------------|--------------------------------
Go to line                                      | `:n` where n is the line number
Go to file                                      | `gf` for Go to File
Open file at line number                        | `vim path/to/file +n` where n is the line number
Go to top of file                               | `gg`
Go to bottom of file                            | `G`
Scroll the screen half way up                   | `CTRL + u` for Up
Scroll the screen half way down                 | `CTRL + d` for Down
Move to next or previous related item           | `%` (Brackets, do/end, etc.)
Toggle between last 2 positions                 | **``** (double backticks)
Jump to previous cursor position                | `CTRL + O`
Jump to next cursor position (after `CTRL + O)  | `CTRL + O`

## Editing

Task                              | Command
----------------------------------|--------------------------------
Delete a character                | `x`
Undo the last command             | `u` 
Redo the last command             | `CTRL + r`
Save                              | `w` for Write
Save and Quit                     | `:wq` or `ZZ`
Trash all changes                 | `:q!`
Quit all                          | `:qa`
Cut                               | `d` for Delete
Cut line                          | `dd`
Copy                              | `y` for Yank
Copy current word                 | `yiw`
Copy line down                    | `yyp`
Paste                             | `p` to paste after the cursor and `P` for before the cursor
Join next line with current line  | `J`
Repeat last command               | `.`

## Tabs

Task                                 | Command
-------------------------------------|--------------------------------
Open multiple files in separate tabs | `vim -p /path/to/file1 /path/file2 file3`
Jump to the next tab                 | `gt` or `:tabn[ext]`
Jump to the previous tab             | `gT` or `:tabp[revious]`
Jump to a specific tab               | `ngt` where n is the tab index starting at 1
Close the current tab                | `:tabc[lose]`

## Later implementations

- https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en
- https://thoughtbot.com/blog/running-specs-from-vim

## References

- https://devhints.io/vim
- https://blog.confirm.ch/mastering-vim-working-with-multiple-files
- https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started
- https://medium.com/usevim/vim-101-quick-movement-c12889e759e0
