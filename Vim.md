# Vim

- [Overview](#overview)
- [Definitions](#definitions)
- [Text objects](#text-objects)
- [Visual mode](#visual-mode)
- [Save & quit](#save--quit)
- [Navigation](#navigation)
- [Clipboard](#clipboard)
- [Insert mode](#insert-mode)
- [Editing](#editing)
- [Search & replace](#search--replace)
- [Spell check](#spell-check)
- [Tabs & splits](#tabs--splits)
- [Later tutorials and implementations](#later-tutorials-and-implementations)
- [References](#references)

## Overview

Vim has two modes:

1. Insert mode (Where you can just type like normal text editor. Press i for insert mode)
2. Command mode (Where you give commands to the editor to get things done. Press` ESC` for command mode)

You can combine the Verbs (commands) and Nouns (motions & text objects) in any way you need.

## Definitions

**Operators** let you operate in a range of text (defined by motion). These are performed in normal mode.
Example:

    dw # d is the Operator, w is the Motion

## Text objects

**Text objects** let you operate (with an operator) in or around text blocks (objects). Example:

    vip # v is the Operator, [i]nside or [a]round, p is the Text Object

| Type             | Command            |
| ---------------- | ------------------ |
| Paragraph        | `p`                |
| Word             | `w`                |
| Sentence         | `s`                |
| Blocks           | `[`, `(`, `{`, `<` |
| A quoted string  | `'`, `"`, `` ` ``  |
| A block [(       | `b`                |
| A block in [{    | `Shift + B`        |
| An XML tag block | `t`                |
| Pattern search   | `/<PATTERN>`       |

## Visual mode

Visual block mode allows for selecting a column of text. To do this:

1. Press `Ctrl + V` to  start selection
1. Press `Shift and I` then type in any text
1. Press `Esc` twice

## Save & quit

| Operation                                 | Mapping                       |
| ----------------------------------------- | ----------------------------- |
| Write (save) the file, but don't exit     | `:w[rite]`                    |
| Write out the current file using sudo     | `:w !sudo tee %`              |
| Write (save) and quit                     | `:wq` or `:x` or `Shift + ZZ` |
| Quit (fails if there are unsaved changes) | `:q`                          |
| Quit and discard unsaved changes          | `:q!` or `Shift + ZQ`         |
| Write (save) and quit on all tabs         | `wqa`                         |

## Navigation

| Operation                                        | Mapping                                                   |
| ------------------------------------------------ | --------------------------------------------------------- |
| Arrow keys                                       | `h`, `j`, `k`, `l`                                        |
| Go to line                                       | `:n` where `n` is the line number                         |
| Go to file                                       | `gf`                                                      |
| Open file at line number                         | `vim path/to/file +n` where `n` is the line number        |
| Go to top of file                                | `gg`                                                      |
| Go to bottom of file                             | `Shift + G`                                               |
| Scroll the screen half way up                    | `CTRL + u`                                                |
| Scroll the screen half way down                  | `CTRL + d`                                                |
| Scroll line to top                               | `zt`                                                      |
| Scroll line to center                            | `zz`                                                      |
| Scroll line to bottom                            | `zb`                                                      |
| Move to next or previous brackets, do/end, etc.  | `%`                                                       |
| Toggle between last 2 positions                  | `` ` ``                                                   |
| Go to previous cursor position                   | `CTRL + Shift + O`                                        |
| Go to next cursor position                       | `CTRL + Shift + I`                                        |
| Go between paragraphs                            | `{` to go back, `}` to go forward                         |
| Go between words                                 | `w` to move forward a word, `b` to move back a word       |
| Go between words with punctuation                | `Shift + W` to move forward, `Shift + B` to move back     |
| Go to end of word                                | `e`                                                       |
| Go to end of word with punctuation               | `Shift + E`                                               |
| Go to character on current line                  | `f<char>`. Press `;` to repeat last jump. `,` for reverse |
| Go until (before) a character on current line    | `t<char>`. Press `;` to repeat last jump. `,` for reverse |
| Go to line's beginning                           | `0`                                                       |
| Go to line's end                                 | `$`                                                       |
| Go to line's first non-blank character           | `^`                                                       |
| Center current line                              | `zz`                                                      |
| Jump forward to begin of next top level          | `]]`                                                      |
| Jump backwards to begin of current top level     | `[[`                                                      |
| Jump forward to begin of next method/scope       | `]m`                                                      |
| Jump backwards to begin of previous method/scope | `[m`                                                      |
| Jump forward to end of current top level         | `][`                                                      |
| Jump backward to end of previous of top level    | `[]`                                                      |
| Jump forward to end of current method/scope      | `]M`                                                      |
| Jump backward to end of previous method/scope    | `[M`                                                      |

## Clipboard

| Operation                     | Mapping                                         |
| ----------------------------- | ----------------------------------------------- |
| Select current paragraph      | `vip`. Keep pressing `ip` to increase selection |
| Cut (delete) a character      | `x`                                             |
| Cut (delete) a line           | `dd`                                            |
| Cut (delete) 2 lines          | `2dd`                                           |
| Copy (yank) a line            | `yy`                                            |
| Copy (yank) current word      | `yiw`                                           |
| Copy (yank) current paragraph | `yip`                                           |
| Copy (yank) line down         | `yyp`                                           |
| Paste after the cursor        | `p`                                             |
| Paste before the cursor       | `Shift + P`                                     |

## Insert mode

| Operation                                       | Mapping     |
| ----------------------------------------------- | ----------- |
| Insert before the cursor                        | `i`         |
| Insert at the beginning of the line             | `Shift + I` |
| Insert (append) after the cursor                | `a`         |
| Insert (append) at the end of the line          | `Shift + A` |
| Insert (append) at the end of the word          | `ea`        |
| Insert (open) a new line below the current line | `o`         |
| Insert (open) a new line above the current line | `Shift + O` |
| Exit insert mode                                | `Esc`       |
| Auto complete using next word                   | `Ctrl + n`  |
| Auto complete using previous word               | `Ctrl + n`  |

## Editing

| Operation                        | Mapping                                         |
| -------------------------------- | ----------------------------------------------- |
| Undo the last command            | `u`                                             |
| Redo the last command            | `CTRL + r`                                      |
| Join next line with current line | `Shift + J`                                     |
| Repeat last command              | `.` _(period)_                                  |
| Sort lines (alphabetically)      | `Shift + V` to visually select lines, `:sort`   |
| Sort lines (numerically)         | `Shift + V` to visually select lines, `:sort n` |
| Indent text right                | `Shift + >`                                     |
| Indent text left                 | `Shift + <`                                     |
| Reformat line                    | `==`                                            |
| Reformat selection               | `=`                                             |
| Reformat entire file             | `gg=G`                                          |
| Character case toggle            | `~`                                             |
| Character case to upper          | `gU`                                            |
| Character case to lower          | `gu`                                            |

## Search & replace

| Operation                                               | Mapping                 |
| ------------------------------------------------------- | ----------------------- |
| Search                                                  | `/<pattern>`            |
| Search case insensitive                                 | `/<pattern>\C`          |
| Repeat last search                                      | `n`                     |
| Repeat last search in opposite direction                | `Shift + N`             |
| Remove highlighting of search matches                   | `:noh`                  |
| Replace old with new throughout file                    | `:%s/old/new/g`         |
| Replace old with new throughout file with confirmations | `:%s/old/new/gc`        |
| Repeat last search and replace                          | `@:` and `@@` to repeat |

## Spell check

| Operation                                               | Mapping        |
| ------------------------------------------------------- | -------------- |
| Move to next misspelled word after the cursor           | `]s`           |
| Move to previous misspelled word before the cursor      | `[s`           |
| z=Suggest spellings for the word under/after the cursor | `z=`           |
| Add word to spell list                                  | `zg`           |
| Enable spell check                                      | `:set spell`   |
| Disable spell check                                     | `:set nospell` |

## Tabs & splits

| Operation                            | Mapping                                                |
| ------------------------------------ | ------------------------------------------------------ |
| Open multiple files in separate tabs | `vim -p /path/to/file1 /path/file2 file3`              |
| Jump to the next tab                 | `gt` or `:tabn[ext]`                                   |
| Jump to the previous tab             | `gT` or `:tabp[revious]`                               |
| Jump to a specific tab               | `ngt` where n is the tab index starting at 1           |
| Close the current tab                | `:tabc[lose]`                                          |
| Move between splits                  | `Ctrl +` one of the movement keys (`h`, `j`, `k`, `l`) |

## Later tutorials and implementations

- https://thoughtbot.com/upcase/the-art-of-vim
- https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en
- https://thoughtbot.com/blog/running-specs-from-vim
- https://github.com/tpope/vim-rails
- https://github.com/thoughtbot/vim-rspec

## References

- https://devhints.io/vim
- https://blog.confirm.ch/mastering-vim-working-with-multiple-files
- https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started
- https://medium.com/usevim/vim-101-quick-movement-c12889e759e0
- https://items.sjbach.com/319/configuring-vim-right
- https://thoughtbot.com/blog/thoughtbot-is-filled-with-vim-and-vigor
- https://vim.rtorr.com/
- https://vim.fandom.com/wiki/Searching
- https://vim.fandom.com/wiki/Search_and_replace
