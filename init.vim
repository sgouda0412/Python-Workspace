" init.vim for Python Full-Stack Development

" General settings
set encoding=UTF-8
set number                " Show line numbers
set relativenumber        " Relative line numbers
set tabstop=4             " Number of spaces a tab counts for
set shiftwidth=4          " Number of spaces to use for autoindent
set expandtab             " Convert tabs to spaces
set autoindent            " Copy indent from current line when starting a new line
set smartindent           " Makes indenting smart
set clipboard=unnamedplus " Use system clipboard
set wrap                  " Wrap long lines
set cursorline            " Highlight the current line
set termguicolors         " Enable 24-bit RGB colors
set background=dark       " Set background to dark for color schemes
syntax on                 " Enable syntax highlighting
filetype plugin indent on " Enable filetype detection, plugin, and indent

" vim-plug setup
call plug#begin('~/.config/nvim/plugged')

" Python development plugins
Plug 'neoclide/coc.nvim', {'branch': 'release'} " coc.nvim for autocompletion, linting, formatting
Plug 'psf/black'                    " Code formatter (Black)
Plug 'tell-k/vim-autopep8'          " AutoPEP8 formatting
Plug 'vim-python/python-syntax'     " Improved Python syntax highlighting

" General development plugins
Plug 'preservim/nerdtree'           " File tree explorer
Plug 'scrooloose/nerdcommenter'     " Easy commenting
Plug 'tpope/vim-fugitive'           " Git integration
Plug 'airblade/vim-gitgutter'       " Git diff in the gutter
Plug 'itchyny/lightline.vim'        " Lightweight status line
Plug 'nvim-tree/nvim-web-devicons'  " Icons for file types
Plug 'scrooloose/nerdcommenter'  " Plugin for commenting code
Plug 'morhetz/gruvbox'
Plug 'tpope/vim-commentary'
Plug 'dense-analysis/ale'
Plug 'ryanoasis/vim-devicons'


" Telescope - Fuzzy Finder
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-lua/plenary.nvim'  " Required for telescope

" LSP Config
Plug 'neovim/nvim-lspconfig'

" Linting and Formatting
Plug 'jose-elias-alvarez/null-ls.nvim'  " For integration with linters like pylint

call plug#end()

" Enable vim-devicons globally
let g:webdevicons_enable = 1

" NERDTree configuration
let g:NERDTreeShowHidden=1
let g:NERDTreeShowBookmarks=1
" coc.nvim Configuration
let g:coc_global_extensions = ['coc-pyright']

" Initialize nvim-web-devicons
lua << EOF
require'nvim-web-devicons'.setup { default = true; }
EOF
" Configure ALE for pylint
let g:ale_linters = {
\   'python': ['pylint'],
\}

" Optional: Display linting errors in a floating window
let g:ale_sign_error = '✗'
let g:ale_sign_warning = '⚠'
let g:ale_virtualtext_cursor = 'enable'
let g:ale_virtualtext_errors = 1
let g:ale_virtualtext_warnings = 1
" Map Ctrl+R to save and run Python code
nnoremap <C-e> :w<CR>:!python3 %<CR>
inoremap <C-e> <Esc>:w<CR>:!python3 %<CR>

" Telescope setup
let g:telescope_defaults = {
\   'file_ignore_patterns': ['node_modules', '.git'],
\ }

" Key mappings for Telescope with Ctrl
nnoremap <C-f> :Telescope find_files<CR>
nnoremap <C-g> :Telescope live_grep<CR>
nnoremap <C-b> :Telescope buffers<CR>
nnoremap <C-h> :Telescope help_tags<CR>


" LSP configuration
" Configure Python LSP (using Pyright as an example)
augroup lsp
  autocmd!
  autocmd FileType python setlocal omnifunc=v:lua.vim.lsp.omnifunc
augroup END

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

" Copy the selected text to clipboard (Ctrl+C)
vnoremap <C-c> "+y
nnoremap <C-c> "+yy

" Paste from clipboard (Ctrl+V)
nnoremap <C-v> "+p
vnoremap <C-v> "+p

" Select all text (Ctrl+A)
nnoremap <C-a> ggVG

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
set background=dark    " Set background to dark mode
colorscheme gruvbox    " Set colorscheme to Gruvbox
" Git Integration
nmap <Leader>gs :Gstatus<CR>
nmap <Leader>gc :Gcommit<CR>
nmap <Leader>gp :Gpush<CR>
nmap <Leader>gl :Gpull<CR>

" Python virtual environment
let g:python3_host_prog = '~/.virtualenvs/neovim3/bin/python'



