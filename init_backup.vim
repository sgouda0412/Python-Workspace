" init.vim for Python Full-Stack Development

" General settings
set encoding=UTF-8
set number                " Show line numbers
set relativenumber        " Relative line numbers
set tabstop=4             " Number of spaces a tab counts for
set shiftwidth=4          " Number of spaces to use for autoindent
set expandtab             " Convert tabs to spaces
set autoindent            " Copy indent from current line when starting a new line
set softtabstop=4
set mouse=a               " Set Mouse to active
set smartindent           " Makes indenting smart
set clipboard=unnamedplus " Use system clipboard
set wrap                  " Wrap long lines
set cursorline            " Highlight the current line
set termguicolors         " Enable 24-bit RGB colors
set background=dark       " Set background to dark for color schemes
set autowriteall
set hlsearch
set incsearch
syntax on                 " Enable syntax highlighting
filetype plugin indent on " Enable filetype detection, plugin, and indent

" vim-plug setup
call plug#begin('~/.config/nvim/plugged')

" Python development plugins
Plug 'neoclide/coc.nvim', {'branch': 'release'} " coc.nvim for autocompletion, linting, formatting
" Plug 'davidhalter/jedi-vim'
Plug 'heavenshell/vim-pydocstring', { 'do': 'make install', 'for': 'python' }
Plug 'psf/black'                    " Code formatter (Black)
Plug 'tell-k/vim-autopep8'          " AutoPEP8 formatting
Plug 'vim-python/python-syntax'     " Improved Python syntax highlighting
Plug 'mhinz/vim-startify'
Plug 'arzg/vim-colors-xcode'
Plug 'SirVer/ultisnips'  " UltiSnips plugin
Plug 'Xuyuanp/scrollbar.nvim'
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
Plug 'navarasu/onedark.nvim'
Plug 'junegunn/limelight.vim' " Limelight - Additional Focus mode stuff with Goyo
Plug 'tpope/vim-surround'
Plug 'vimwiki/vimwiki'
Plug 'skywind3000/vim-keysound'
Plug 'romgrk/barbar.nvim'
Plug 'preservim/tagbar'
Plug 'rebelot/kanagawa.nvim'
Plug 'sainnhe/sonokai'
Plug 'cameron-wags/rainbow_csv.nvim'
Plug 'lalitmee/cobalt2.nvim'
Plug 'vim-test/vim-test'
Plug 'tpope/vim-dadbod'
Plug 'kristijanhusak/vim-dadbod-ui'
Plug 'kristijanhusak/vim-dadbod-completion'
Plug 'b4b4r07/vim-sqlfmt'
Plug 'jackMort/ChatGPT.nvim', { 'do': 'pip install -r requirements.txt' }
Plug 'skywind3000/vim-rt-format'
Plug 'nvim-treesitter/nvim-treesitter', { 'commit': 'COMMIT_HASH' }
Plug 'junegunn/goyo.vim' " Focus Mode
Plug 'nvim-lua/plenary.nvim'
" LeetCode Plugin

" LeetCode Plugin
Plug 'kawre/leetcode.nvim'

" Dependencies for LeetCode.nvim
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'MunifTanjim/nui.nvim'

" Optional Plugins
Plug 'nvim-treesitter/nvim-treesitter'
Plug 'rcarriga/nvim-notify'
Plug 'nvim-tree/nvim-web-devicons'

"Plug 'MunifTanjim/nui.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'folke/trouble.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'MunifTanjim/nui.nvim'
"Plug 'MunifTanjim/nui.nvim', { 'commit': 'commit_hash_here' }
"Plug 'xemptuous/sqlua.nvim'
"Plug 'kndndrj/nvim-dbee'
"Plug 'MunifTanjim/nui.nvim'
"Plug 'javiorfo/nvim-tabula'
"Plug 'javiorfo/nvim-popcorn'
"Plug 'javiorfo/nvim-spinetta'
" General development plugins
Plug 'preservim/nerdtree'           " File tree explorer
Plug 'scrooloose/nerdcommenter'     " Easy commenting
Plug 'tpope/vim-fugitive'           " Git integration
Plug 'airblade/vim-gitgutter'       " Git diff in the gutter
Plug 'itchyny/lightline.vim'        " Lightweight status line
" Plug 'nvim-tree/nvim-web-devicons'  " Icons for file types
Plug 'scrooloose/nerdcommenter'  " Plugin for commenting code
Plug 'morhetz/gruvbox'
Plug 'tpope/vim-commentary'
Plug 'dense-analysis/ale'
Plug 'ryanoasis/vim-devicons'
Plug 'Mofiqul/vscode.nvim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'  " Optional: Additional themes for vim-airline
Plug 'blueshirts/darcula'
Plug 'akinsho/toggleterm.nvim', {'tag': '*'}
Plug 'Vimjas/vim-python-pep8-indent'
" Telescope - Fuzzy Finder
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-lua/plenary.nvim'  " Required for telescope
Plug 'w0rp/ale'  " python linters
" LSP Config
Plug 'neovim/nvim-lspconfig'
Plug 'devsjc/vim-jb'
Plug 'projekt0n/github-nvim-theme'
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
Plug 'EdenEast/nightfox.nvim' " Vim-Plug
Plug 'maxmx03/solarized.nvim'
Plug 'rktjmp/lush.nvim'
Plug 'rockyzhang24/arctic.nvim', { 'branch': 'v2' }
" Linting and Formatting
" Plug 'jose-elias-alvarez/null-ls.nvim'  " For integration with linters like pylint
" Debugging
Plug 'nvim-telescope/telescope-dap.nvim'
Plug 'mfussenegger/nvim-dap'
Plug 'mfussenegger/nvim-dap-python'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'cdmill/neomodern.nvim'
" Plug 'mfussenegger/nvim-dap'
Plug 'theHamsta/nvim-dap-virtual-text'
Plug 'nvim-neotest/nvim-nio'
Plug 'rcarriga/nvim-dap-ui'
" Plug 'mfussenegger/nvim-dap-python'
"Plug 'dinhhuy258/vim-database', {'branch': 'master', 'do': ':UpdateRemotePlugins'}
Plug 'folke/zen-mode.nvim'
Plug 'YacineDo/mc.nvim'
Plug 'kdheepak/lazygit.nvim'
" Plug 'hrsh7th/nvim-cmp'              " Completion engine
" Plug 'hrsh7th/cmp-nvim-lsp'           " LSP source for nvim-cmp
" Plug 'hrsh7th/cmp-buffer'             " Buffer completions
" Plug 'hrsh7th/cmp-path'               " Path completions
" SQL syntax highlighting
" Plug 'lifepillar/vim-sql-syntax'
" Plug 'nanotee/sqls.nvim'
" Plug 'hrsh7th/cmp-cmdline'            " Cmdline completions

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
call plug#end()

lua << EOF
require("notify").setup({
    background_colour = "#000000",  -- Set your desired background color
})

-- vim.cmd("highlight NotifyBackground guibg=#002b36 ctermbg=235"-- Ensure the highlight group has a background
EOF

" Build command for treesitter HTML support
autocmd VimEnter * TSUpdate html

" LeetCode.nvim Configuration
let g:leetcode_browser = 'chrome'                    " Set your preferred browser for discussions
let g:leetcode_solution_filetype = 'python'          " Default filetype for solutions
let g:leetcode_workspace = '~/leetcode'              " Directory to store LeetCode solutions

" LeetCode.nvim Options
lua << EOF
require('leetcode').setup {
    lang = "python",  -- Default language (change as needed)
    storage = {
        home = vim.fn.stdpath("data") .. "/leetcode",  -- Storage directory
        cache = vim.fn.stdpath("cache") .. "/leetcode", -- Cache directory
    },
    theme = {
        alt = {
            bg = "#002b36",  -- Background color
        },
        normal = {
            fg = "#FFFFFF",  -- Foreground color
        },
    },
    cn = {
        enabled = false,  -- Enable for leetcode.cn
        translator = true,
        translate_problems = true,
    },
    cache = {
        update_interval = 60 * 60 * 24 * 7,  -- Cache update interval (7 days)
    },
    description = {
        position = "left",
        width = "40%",
        show_stats = true,
    },
    console = {
        open_on_runcode = true,
        size = {
            width = "90%",
            height = "75%",
        },
        result = {
            size = "60%",
        },
        testcase = {
            virt_text = true,
            size = "40%",
        },
    },
    logging = true,
    hooks = {
        enter = {},
        question_enter = {},
        leave = {},
    },
    injector = {
        python3 = {
            before = true,  -- Inject default imports for Python3
        },
        cpp = {
            before = { "#include <bits/stdc++.h>", "using namespace std;" },
            after = "int main() {}",
        },
        java = {
            before = "import java.util.*;",
        },
    },
    keys = {
        toggle = { "q" },  -- Keybinding for toggling description
        confirm = { "<CR>" },  -- Keybinding for confirming selection
    },
}
EOF

"autocmd BufEnter * if bufname('%') == '' | enew | endif

" Custom Key Mappings
nnoremap <leader>lm :Leet<CR>                       " Open LeetCode dashboard menu
nnoremap <leader>lt :Leet run<CR>                   " Test your solution
nnoremap <leader>ls :Leet submit<CR>                " Submit your solution
nnoremap <leader>li :Leet signin<CR>                " Sign into LeetCode
nnoremap <leader>lo :Leet info<CR>                  " Show current problem info
nnoremap <leader>lr :Leet random<CR>                " Open a random question
nnoremap <leader>ld :Leet daily<CR>                 " Open today's LeetCode question
nnoremap <leader>ll :Leet list<CR>                  " List problems
"vim.api.nvim_set_keymap('n', '<leader>tn', '<Plug>(LeetCodeNextTest)', { noremap = true, silent = true })  -- Move to the next test case
"vim.api.nvim_set_keymap('n', '<leader>tp', '<Plug>(LeetCodePrevTest)', { noremap = true, silent = true })  -- Move to the previous test case
" vim-dadbod
"autocmd FileType sql,mysql,plsql lua require('cmp').setup.buffer({ sources = {% raw %}{{ name = 'vim-dadbod-completion' }}{% endraw %} })
let g:db_ui_save_location = '~/.config/nvim/dadbod-ui'
let g:db_ui_show_database_icon = 1
"let g:db_ui_use_nerd_fonts = 1
let g:db_ui_force_echo_notifications = 1
let g:db_ui_winwidth = 30
let g:db_ui_icons = {
    \ 'expanded': '▾',
    \ 'collapsed': '▸',
    \ 'saved_query': '*',
    \ 'new_query': '+',
    \ 'tables': '~',
    \ 'buffers': '»',
    \ 'connection_ok': '✓',
    \ 'connection_error': '✕',
    \ }
let g:dbs = {
    \ 'mysql': 'mysql://root:root@localhost/sqlpractices'
\ }
" Keybinding to show results in a popup window

" vim-dadbod-ui key mappings
nmap <leader>dt :DBUIToggle<CR>
nmap <leader>da :DBUIAddConnection<CR>
nmap <leader>df :DBUIFindBuffer<CR>
nmap <leader>dr :DBUIRenameBuffer<CR>
nmap <leader>dl :DBUILastQueryInfo<CR>
nmap <leader>dp :call ShowDBResultInPopup()<CR>
"nmap <leader>dq :DB vert split<CR>   " Vertical split
"nmap <leader>dh :DB split<CR>        " Horizontal split
"nmap <leader>dt :tab DB<CR>          " Open result in a new tab
"nmap <leader>du :DBUI | vsplit<CR>   " Toggle UI in split window
"autocmd FileType dbui setlocal norelativenumber
" Disable relative numbers in DBUI buffers
augroup DBUI
    autocmd!
    autocmd BufEnter * if &filetype == 'dbui' | setlocal norelativenumber | endif
augroup END

" Enable absolute line numbers in DBUI
augroup DBUIAbsoluteNumbers
    autocmd!
    autocmd BufEnter * if &filetype == 'dbui' | setlocal number | endif
augroup END
" autocmd FileType sql setlocal omnifunc=v:lua.vim.lsp.omnifunc
autocmd FileType sql setlocal omnifunc=vim_dadbod_completion#omni

"=================================="
"             VIM WIKI             "
"=================================="
    " ~~~~~ Ensure files are read as what I want in vimwiki:
        autocmd FileType vimwiki setlocal filetype=vimwiki
        let g:vimwiki_global_ext = 0
        let g:vimwiki_table_mappings = 0
        let g:vimwiki_ext2syntax = {'.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
        let g:vimwiki_root = '~/VimWiki'
        let g:vimwiki_listsyms = '✗○◐●✓'
        let g:vimwiki_list = [
            \{'path': '~/VimWiki', 'syntax': 'markdown', 'ext': '.md'},
            \{'path': '~/VimWiki/academia', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/academia/statistics', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/social', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/spirituality', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/linux', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/c', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/css', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/bash', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/html', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/latex', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/r', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/regex', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/rust', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/VimWiki/tech/python', 'syntax': 'markdown', 'ext':'.md'},
            \{'path': '~/.config/mynotes/','syntax': 'markdown', 'ext': '.mdvimwiki'}]
"=================================="
"              GOYO                "
"=================================="
        " ~~~~~ Goyo plugin makes text more readable when writing prose:
                let g:goyo_width=200
                map <leader>gy :Goyo \| set bg=dark \| set linebreak<CR>
                map <leader>ll :Limelight!!<CR>
        " ~~~~~ Enable Goyo by default for mutt writting
        " ~~~~~ Goyo's width will be the line limit in mutt.
                autocmd BufRead,BufNewFile /tmp/neomutt* let g:goyo_width=80
                autocmd BufRead,BufNewFile /tmp/neomutt* :Goyo \| set bg=light
                autocmd BufRead,BufNewFile /tmp/neomutt* map ZZ :Goyo\|x!<CR>
                autocmd BufRead,BufNewFile /tmp/neomutt* map ZQ :Goyo\|q!<CR>

"=================================="
"           LimeLight              "
"=================================="
        " ~~~~~ Color name (:help cterm-colors) or ANSI code
                let g:limelight_conceal_ctermfg = 'gray'
                let g:limelight_conceal_ctermfg = 240
        " ~~~~~ Color name (:help gui-colors) or RGB color
                let g:limelight_conceal_guifg = 'DarkGray'
                let g:limelight_conceal_guifg = '#777777'
        " ~~~~~ Default: 0.5
                let g:limelight_default_coefficient = 0.7
        " ~~~~~ Number of preceding/following paragraphs to include (default: 0)
                let g:limelight_paragraph_span = 1
        " ~~~~~ Beginning/end of paragraph
        " ~~~~~ When there's no empty line between the paragraphs
        " ~~~~~ and each paragraph starts with indentation
                let g:limelight_bop = '^\s'
                let g:limelight_eop = '\ze\n^\s'
        " ~~~~~ Highlighting priority (default: 10)
        " ~~~~~ Set it to -1 not to overrule hlsearch
                let g:limelight_priority = -1
        " ~~~~~ Integration with goyo
                autocmd! User GoyoEnter Limelight
                autocmd! User GoyoLeave Limelight! \| set bg=light
"=================================="


let g:keysound_py_version = 3
let g:keysound_enable = 1
let g:keysound_theme = 'typewriter'
let g:rtf_ctrl_enter = 0
let g:rtf_on_insert_leave = 1
augroup ScrollbarInit
  autocmd!
  autocmd WinScrolled,VimResized,QuitPre * silent! lua require('scrollbar').show()
  autocmd WinEnter,FocusGained           * silent! lua require('scrollbar').show()
  autocmd WinLeave,BufLeave,BufWinLeave,FocusLost            * silent! lua require('scrollbar').clear()
augroup end
" ChatGPT configuration
let g:chatgpt_default_prompt = "How can I help you today?"

" Keybindings for ChatGPT.nvim


" ChatGPT.nvim configuration
lua << EOF
require("chatgpt").setup({
    api_key_cmd = "echo -n $OPENAI_API_KEY",  -- Adjust this line for your key management
    openai_params = {
        model = "gpt-3.5-turbo",  -- Change the model as needed
        frequency_penalty = 0,
        presence_penalty = 0,
        max_tokens = 4095,
        temperature = 0.2,
        top_p = 0.1,
        n = 1,
    }
})
EOF

" Key mappings for ChatGPT commands
nnoremap <leader>c <cmd>ChatGPT<CR>
nnoremap <leader>e <cmd>ChatGPTEditWithInstructions<CR>
nnoremap <leader>g <cmd>ChatGPTRun grammar_correction<CR>
nnoremap <leader>t <cmd>ChatGPTRun translate<CR>
nnoremap <leader>k <cmd>ChatGPTRun keywords<CR>
nnoremap <leader>d <cmd>ChatGPTRun docstring<CR>
nnoremap <leader>a <cmd>ChatGPTRun add_tests<CR>
nnoremap <leader>o <cmd>ChatGPTRun optimize_code<CR>
nnoremap <leader>s <cmd>ChatGPTRun summarize<CR>
nnoremap <leader>f <cmd>ChatGPTRun fix_bugs<CR>
nnoremap <leader>x <cmd>ChatGPTRun explain_code<CR>
nnoremap <leader>r <cmd>ChatGPTRun roxygen_edit<CR>
nnoremap <leader>l <cmd>ChatGPTRun code_readability_analysis<CR>


nnoremap <leader>cg :ChatGPT<CR>          " Trigger ChatGPT
nnoremap <leader>cq :ChatGPTAsk<CR>       " Ask a question
nnoremap <leader>cc :ChatGPTCodeComplete<CR> " Complete code
vnoremap <leader>ce :ChatGPTEditWithInstructions<CR> " Edit selection


" Load and configure Zen Mode
lua << EOF
require("zen-mode").setup {
  -- Add any custom configurations here, like window width, etc.
  window = {
    width = 200, -- width of the Zen window
  }
}
EOF

" Key mapping to toggle Zen Mode with F5
nnoremap <C-A-z> :ZenMode<CR>
" Configure lazygit settings
let g:lazygit_floating_window_winblend = 0         " Transparency of floating window
let g:lazygit_floating_window_scaling_factor = 0.9 " Scaling factor for floating window
let g:lazygit_floating_window_border_chars = ['╭','─', '╮', '│', '╯','─', '╰', '│'] " Border characters
let g:lazygit_floating_window_use_plenary = 0      " Use plenary.nvim if available
let g:lazygit_use_neovim_remote = 1                " Fallback to 0 if neovim-remote is not installed
let g:lazygit_use_custom_config_file_path = 0      " Set to 1 to use custom config file
let g:lazygit_config_file_path = ''                " Define custom config file path (if needed)

" Setup mapping to call :LazyGit
nnoremap <silent> <C-A-j> :LazyGit<CR>

""""""""""""""""""""""""""""""""""""'
" SQL Formatting
""""""""""""""""""""""""""""""""""""'
let g:sqlfmt_command = "sqlformat"
let g:sqlfmt_options = ""

" Create cursors vertically with Ctrl-Down/Ctrl-Up
nnoremap <C-Down> :MCAddCursorDown<CR>
nnoremap <C-Up> :MCAddCursorUp<CR>

" Treesitter setup using Lua
lua << EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = { "python", "lua", "javascript" },  -- List of parsers to install
  highlight = {
    enable = true,               -- false will disable the whole extension
    additional_vim_regex_highlighting = false,
  },
}
EOF

let g:vim_database_rows_limit = 50
let g:vim_database_window_layout = "below"



nnoremap <leader>du :DBUIToggle<CR>
nnoremap <leader>dr :DBUIRenameBuffer<CR>
nnoremap <leader>dq :DBUIExecuteQuery<CR>  " Execute query

" Map Ctrl + d to toggle the database view
"nnoremap <silent> <C-m> :VDToggleDatabase<CR>

" Map Ctrl + q to toggle the query view
"nnoremap <silent> <C-k> :VDToggleQuery<CR>

" Map Ctrl + f to list tables with FZF
"nnoremap <silent> <C-g> :VimDatabaseListTablesFzf<CR>


" vim-test configurations
let test#strategy = "neovim"  " Use Neovim's built-in terminal
let test#python#runner = 'pytest'

" Keybindings for vim-test
nmap <silent> <leader>t :TestNearest<CR>
nmap <silent> <leader>f :TestFile<CR>
nmap <silent> <leader>a :TestSuite<CR>
nmap <silent> <leader>l :TestLast<CR>
nmap <silent> <leader>g :TestVisit<CR>


" Map Tab to insert 4 spaces in insert mode
inoremap <Tab> <C-T>
filetype plugin on
autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4 expandtab
let g:pydocstring_doq_path = '/home/sgouda/.virtualenvs/neovim3/bin/doq'
" Generate docstring for the function or class under the cursor
nnoremap <C-P> :Pydocstring<CR>
let g:pydocstring_enable_mapping = 0
let g:pydocstring_formatter = 'google'
let g:pydocstring_ignore_init = 1
let g:pydocstring_templates_path = '~/.config/nvim/doc'

" vim-python-pep8-indent configurations
let g:python_pep8_indent_multiline_string = 1
let g:python_pep8_indent_hang_closing = 0

" Additional Python indentation settings
autocmd FileType python setlocal indentkeys+=<:>,=elif,=except
autocmd BufWritePre * :%s/\s\+$//e

" Key mappings for vim-python-pep8-indent
autocmd FileType python nnoremap <buffer> == :call Preserve("normal gg=G")<CR>
autocmd FileType python vnoremap <buffer> = :call Preserve("normal gv=")<CR>

" Function to preserve cursor position when re-indenting
function! Preserve(command)
    " Save last search, and cursor position.
    let _s=@/
    let l = line(".")
    let c = col(".")
    " Do the business:
    execute a:command
    " Clean up: restore previous search history, and cursor position
    let @/=_s
    call cursor(l, c)
endfunction


" Set this variable to 1 to fix files when you save them.
let g:ale_fix_on_save = 1

" Enable vim-devicons globally
let g:webdevicons_enable = 1

" NERDTree configuration
let g:NERDTreeShowHidden=1
let g:NERDTreeShowBookmarks=1

" Initialize nvim-web-devicons
lua << EOF
require'nvim-web-devicons'.setup { default = true; }
EOF
" Configure ALE to use multiple linters and type checkers for Python
let g:ale_linters = {
\   'python': ['flake8','pyright', 'bandit', 'mypy'],
\}

" Configure fixers for Python
let g:ale_fixers = {
\   '*': ['trim_whitespace', 'remove_trailing_lines'],
\   'python': ['black', 'isort', 'autopep8'],
\}

let g:ale_enabled = 1
let g:ale_lint_on_text_changed = 'always'
let g:ale_lint_on_insert_leave = 1

" Modify ALE Ruff linter command to use 'ruff check'
" let g:ale_python_ruff_options = 'check'

" Automatically fix linting issues on save
let g:ale_fix_on_save = 1


" Customize linting symbols for ALE
let g:ale_sign_error = '🚨'
let g:ale_sign_warning = '💡'
let g:ale_sign_info = '🔍'
let g:ale_sign_hint = '🔔'

" Highlight issues with underlines
highlight ALEErrorSign guifg=red
highlight ALEWarningSign guifg=yellow
highlight ALEInfoSign guifg=blue
highlight ALEHintSign guifg=green

" Python-specific settings
autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4 expandtab

" Enable ALE to fix linting issues on save
let g:ale_fix_on_save = 1
let g:ale_enable = 1
let g:ale_python_flake8_use_global = 0


" Configure flake8 settings
let g:ale_python_flake8_executable = '/home/sgouda/.virtualenvs/neovim3/bin/flake8'
"let g:ale_python_flake8_options = ''
let g:ale_python_flake8_options = '--max-line-length=120' " Set max line length to 79 characters
"let g:ale_python_flake8_options = '--ignore=D100,D102'  " Add your warning/error codes
let g:ale_python_flake8_options = '--ignore=D100,D101,D102,D103,D104,D107,E501'
" Configure bandit settings
let g:ale_python_bandit_executable = 'bandit'
let g:ale_python_bandit_options = '-r'

" Configure pydocstyle settings
let g:ale_python_pydocstyle_executable = 'pydocstyle'
let g:ale_python_pydocstyle_options = ''

" Configure mypy settings
let g:ale_python_mypy_executable = 'mypy'
let g:ale_python_mypy_options = '--ignore-missing-imports'


" Set black and isort as the default fixers
let g:ale_python_black_executable = 'black'
let g:ale_python_black_options = '--line-length 120'

let g:ale_python_isort_executable = 'isort'
let g:ale_python_isort_options = '--profile black'


" Map Ctrl+R to save and run Python code
nnoremap <C-e> :w<CR>:!python3 %<CR>
inoremap <C-e> <Esc>:w<CR>:!python3 %<CR>

map <F6> :colorscheme gruvbox<CR>
map <F7> :colorscheme vscode<CR>
map <F9> :colorscheme kanagawa-dragon<CR>

" tagbar {{{
  map <F8> :TagbarToggle<CR>

  let g:tagbar_autofocus=1
  let g:tagbar_sort=0
  let g:tagbar_type_go = {
      \ 'ctagstype' : 'go',
      \ 'kinds'     : [
          \ 'p:package',
          \ 'i:imports:1',
          \ 'c:constants',
          \ 'v:variables',
          \ 't:types',
          \ 'n:interfaces',
          \ 'w:fields',
          \ 'e:embedded',
          \ 'm:methods',
          \ 'r:constructor',
          \ 'f:functions'
      \ ],
      \ 'sro' : '.',
      \ 'kind2scope' : {
          \ 't' : 'ctype',
          \ 'n' : 'ntype'
      \ },
      \ 'scope2kind' : {
          \ 'ctype' : 't',
          \ 'ntype' : 'n'
      \ },
      \ 'ctagsbin'  : 'gotags',
      \ 'ctagsargs' : '-sort -silent'
  \ }

" }}}


" Telescope setup
let g:telescope_defaults = {
\   'file_ignore_patterns': ['node_modules', '.git'],
\ }

" Key mappings for Telescope with Ctrl
nnoremap <A-f> :Telescope find_files<CR>
nnoremap <A-g> :Telescope live_grep<CR>
nnoremap <A-b> :Telescope buffers<CR>
nnoremap <A-h> :Telescope help_tags<CR>

let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
" Tab Management with Ctrl + Shift
nnoremap <C-S-Right> :tabn<CR>    " Move to the next tab
nnoremap <C-S-Left> :tabp<CR>     " Move to the previous tab
nnoremap <C-S-Up> :tabnew<CR>      " Open a new tab
nnoremap <C-S-Down> :tabc<CR>        " Close the current tab
" Basic UltiSnips configuration
let g:UltiSnipsExpandTrigger="<Tab>"   " Use <Tab> to expand snippets
let g:UltiSnipsJumpForwardTrigger="<tab>"   " Use Ctrl-b to jump forward in snippet
let g:UltiSnipsJumpBackwardTrigger="<S-tab>"   " Use Ctrl-z to jump backward in snippet
" Set custom path for UltiSnips snippets
let g:UltiSnipsSnippetDirectories = ['~/.config/nvim/UltiSnips']
let g:UltiSnipsEditSplit="vertical"

" Basic configuration for toggleterm.nvim
let g:toggleterm_terminal_mapping = '<C-t>'
let g:toggleterm_size = 20
let g:toggleterm_open_mapping = '<C-\\>'
let g:toggleterm_direction = 'horizontal'
" Load and configure toggleterm.nvim

lua << EOF
require("toggleterm").setup({
  size = 20, -- Size of the terminal window
  open_mapping = [[<C-j>]], -- Key mapping to toggle the terminal
  shade_filetypes = {},
  shade_terminals = true,
  shading_factor = 2, -- Darker the background
  start_in_insert = true,
  persist_size = true,
  direction = 'horizontal', -- Can be 'horizontal', 'vertical', or 'float'
})
EOF

" Keybindings for ToggleTerm
nnoremap <C-j> :ToggleTerm<CR>
tnoremap <C-j> <C-\><C-n>:ToggleTerm<CR>

" Normal mode: Select the entire current line using Ctrl + L
nnoremap <C-l> V

" Insert mode: Select the entire current line and return to insert mode
inoremap <C-l> <Esc>Vg_o

" Visual mode: Re-select the entire current line using Ctrl + L
vnoremap <C-l> V


"    settings = {
"        pylsp = {
"            plugins = {
"                pylint = { enabled = true },
"            },
"        },
"    },
"}
"vim.diagnostic.config({
"  virtual_text = {
"    prefix = '●',
"  },
"})
"-- Customize LSP diagnostics colors
"vim.cmd [[
"  highlight LspDiagnosticsDefaultError guifg=Red ctermfg=Red
"  highlight LspDiagnosticsDefaultWarning guifg=Yellow ctermfg=Yellow
"  highlight LspDiagnosticsDefaultInformation guifg=Blue ctermfg=Blue
"]]
"EOF


set hlsearch
"----------------------------------------------
" Splits
"----------------------------------------------
" Create horizontal splits below the current window
set splitbelow
set splitright

" Creating splits with Ctrl + s
nnoremap <F2> :vsplit<cr>  " Vertical split
nnoremap <F3> :split<cr>   " Horizontal split

" Closing splits with Ctrl + s + q
nnoremap <F4> :close<cr>   " Close split

" Map Ctrl + d to delete all content in the buffer
nnoremap <C-d> :%d<CR>

nnoremap <F5> :source ~/.config/nvim/init.vim<CR>

" LSP configuration
" Configure Python LSP (using Pyright as an example)
" augroup lsp
"   autocmd!
"   autocmd FileType python setlocal omnifunc=v:lua.vim.lsp.omnifunc
" augroup END

" Null-ls configuration for pylint
" This is more complex in Vimscript, so this example assumes you use a Lua configuration
" Here is an example of Lua configuration you can add to a separate Lua file and source it
" Use: :luafile ~/.config/nvim/lua/null-ls-config.lua

" Undo and Redo Mappings

" Normal Mode
nnoremap <C-z> u         " Undo with Ctrl+Z
nnoremap <C-r> <C-r>    " Redo with Ctrl+R

" Insert Mode
" Insert Mode
inoremap <silent> <C-z> <Esc>ua
inoremap <silent> <C-r> <Esc><C-r>a
" Visual Mode
xnoremap <C-z> :<C-U>call VisualUndo()<CR> " Undo in Visual Mode
xnoremap <C-r> :<C-U>call VisualRedo()<CR> " Redo in Visual Mode

" Function for Undo in Visual Mode
function! VisualUndo()
    let old_reg = getreg('"')
    let old_sel = &selection
    set selection=exclusive
    let reg = getreg('"')
    execute 'normal! gv"zy'
    let reg = getreg('"')
    let sel = &selection
    set selection=inclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    set selection=exclusive
endfunction

" Function for Redo in Visual Mode
function! VisualRedo()
    let old_reg = getreg('"')
    let old_sel = &selection
    set selection=exclusive
    let reg = getreg('"')
    execute 'normal! gv"zy'
    let reg = getreg('"')
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
    execute 'normal! "zy'
    let sel = &selection
    set selection=exclusive
endfunction




" Single Key Mappings for Moving Between Modes

" Switch to Normal Mode with 'n'
inoremap <C-n> <Esc>
vnoremap <C-n> <Esc> n <Esc>

" Switch to Insert Mode with 'i'
nnoremap i i

" Switch to Visual Mode with 'v'
nnoremap v v

" Optional: To make the transitions smoother
" In Visual Mode, 'i' will switch to Insert Mode
vnoremap i <Esc>i



" Keymaps mimicking VS Code

" Save the current file (Ctrl+S)
function! SaveFile()
    if &buftype == ''
        write
    endif
endfunction

nnoremap <C-s> :call SaveFile()<CR>
inoremap <C-s> <Esc>:call SaveFile()<CR>a

" Run Black formatter (Ctrl+Shift+I)
nnoremap <C-S-i> :Black<CR>
inoremap <C-S-i> <Esc>:Black<CR>a

" Clipboard settings
set clipboard=unnamedplus

" Undo settings
set undofile
set undodir=~/.config/nvim/undodir

" Copy, Paste, Cut, Undo, Redo key mappings
" Copy (yank)
nnoremap <C-c> "+y
vnoremap <C-c> "+y
inoremap <C-c> <C-o>"+y

" Paste
nnoremap <C-v> "+p
vnoremap <C-v> "+p
inoremap <C-v> <C-r><C-o>+

" Cut
nnoremap <C-x> "+d
vnoremap <C-x> "+d
inoremap <C-x> <C-o>"+d

" Undo
nnoremap <C-z> u
vnoremap <C-z> <Esc>u
inoremap <C-z> <C-o>u

" Redo
nnoremap <C-y> <C-r>
vnoremap <C-y> <Esc><C-r>
inoremap <C-y> <C-o><C-r>

" Select all
nnoremap <C-a> ggVG
vnoremap <C-a> <Esc>ggVG
inoremap <C-a> <Esc>ggVG

" Python-specific settings
autocmd FileType python setlocal colorcolumn=180
autocmd FileType python setlocal completeopt-=preview


" Comment/Uncomment code (Ctrl+/)
" Requires nerdcommenter plugin
vnoremap <C-_> :<C-u>call nerdcommenter#Comment(0, "toggle")<CR>
nnoremap <C-_> :<C-u>call nerdcommenter#Comment(0, "toggle")<CR>


" Use <Tab> and <S-Tab> for completion in coc.nvim
inoremap <silent><expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <silent><expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<C-h>"
inoremap <expr> <CR> pumvisible() ? "\<C-Y>" : "\<CR>"
" Auto format on save using Black or AutoPEP8
autocmd BufWritePre *.py execute ':Black'
" or
" autocmd BufWritePre *.py execute ':Autopep8'

" NERDTree Configuration
nmap <C-b> :NERDTreeToggle<CR>
" Find the current file in NERDTree with Ctrl+f
nmap <C-f> :NERDTreeFind<CR>
" Close NERDTree with Ctrl+c
nmap <C-c> :NERDTreeClose<CR>
" Focus on NERDTree with Ctrl+t
nmap <C-t> :NERDTreeFocus<CR>
" Lightline Status Line Configuration
"set background=dark   " Set backgound to dark mode
"set background=dark
set background=dark
"colorscheme gruvbox " Set colorscheme to Gruvbox
"colorscheme github_light
"colorscheme github_dark_default
"colorscheme catppuccin-latte
"colorscheme catppuccin-mocha
"colorscheme solarized
"colorscheme sonokai
"colorscheme kanagawa-dragon
"let g:jb_style='mid'
"colorscheme cobalt2
colorscheme onedark

" Git Integration
nmap <Leader>gs :Gstatus<CR>
nmap <Leader>gc :Gcommit<CR>
nmap <Leader>gp :Gpush<CR>
nmap <Leader>gl :Gpull<CR>
let mapleader = '\'
let maplocalleader = '\'
" Debugging
"lua << EOF
"require('telescope').load_extension('dap')
"require('dap-python').setup('~/.virtualenvs/neovim3/bin/python')
"EOF

lua << EOF
-- DAP Setup
require('dap-python').setup('~/.virtualenvs/neovim3/bin/python')  -- Set your Python path here
require('dapui').setup()

-- Key mappings for DAP
-- vim.api.nvim_set_keymap("n", "<leader>b", ":DapToggleBreakpoint<CR>", {noremap=true})
-- vim.api.nvim_set_keymap("n", "<leader>c", ":DapContinue<CR>", {noremap=true})
-- vim.api.nvim_set_keymap('n', '<leader>o', ':lua require("dapui").open()<CR>', { noremap = true, silent = true })

-- Key mappings for DAP with Ctrl + Alt
vim.api.nvim_set_keymap("n", "<C-A-b>", ":DapToggleBreakpoint<CR>", {noremap=true, silent=true})    -- Ctrl + Alt + B: Toggle breakpoint
vim.api.nvim_set_keymap("n", "<C-A-c>", ":DapContinue<CR>", {noremap=true, silent=true})            -- Ctrl + Alt + C: Continue debugging
vim.api.nvim_set_keymap("n", "<C-A-o>", ':lua require("dapui").open()<CR>', {noremap=true, silent=true})  -- Ctrl + Alt + O: Open DAP UI
vim.api.nvim_set_keymap("n", "<C-A-q>", ':lua require("dapui").close()<CR>', {noremap=true, silent=true}) -- Ctrl + Alt + Q: Close DAP UI

-- Step over, into, out, and restart
vim.api.nvim_set_keymap("n", "<C-A-n>", ":DapStepOver<CR>", {noremap=true, silent=true})            -- Ctrl + Alt + N: Step over
vim.api.nvim_set_keymap("n", "<C-A-i>", ":DapStepInto<CR>", {noremap=true, silent=true})            -- Ctrl + Alt + I: Step into
vim.api.nvim_set_keymap("n", "<C-A-u>", ":DapStepOut<CR>", {noremap=true, silent=true})             -- Ctrl + Alt + U: Step out
vim.api.nvim_set_keymap("n", "<C-A-r>", ":DapRestart<CR>", {noremap=true, silent=true})             -- Ctrl + Alt + R: Restart session
vim.api.nvim_set_keymap("n", "<C-A-s>", ":DapTerminate<CR>", {noremap=true, silent=true})           -- Ctrl + Alt + S: Stop/terminate session

-- Conditional breakpoints and log points
vim.api.nvim_set_keymap("n", "<C-A-l>", ":lua require'dap'.set_breakpoint(nil, nil, vim.fn.input('Log point message: '))<CR>", {noremap=true, silent=true})  -- Ctrl + Alt + L: Set log point
vim.api.nvim_set_keymap("n", "<C-A-d>", ":lua require'dap'.set_breakpoint(vim.fn.input('Breakpoint condition: '))<CR>", {noremap=true, silent=true})          -- Ctrl + Alt + D: Conditional breakpoint

-- DAP REPL (interactive shell)
vim.api.nvim_set_keymap("n", "<C-A-p>", ":DapToggleRepl<CR>", {noremap=true, silent=true})         -- Ctrl + Alt + P: Toggle REPL

EOF


" Python virtual environment
let g:python3_host_prog = '~/.virtualenvs/neovim3/bin/python'
