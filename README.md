[issue]: https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/issues/39
[repo]: https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin

# mkdocs-pagenav-generator
This plugin was created by @lukasgeiter after [I made an issue][issue] on his [awesome-pages plugin Repository][repo] asking about whether it is doable or not to have a setup to create a navigation similar to the TOC-plugin's `[toc]` option to display any pages, that are defined in the `.pages.yml` file of Awesome-pages inside the same directory.

The result is this rather small plugin that *should* achieve this goal.

## Setup
In order to use this plugin will you need to install it using pip:  
```
pip install git+https://github.com/Andre601/mkdocs-pagenav-generator
```

Note that this plugin depends on the Awesome-pages plugin, which you need to install first if you haven't done this already:  
```
pip install mkdocs-awesome-pages-plugin
```

## Usage
In order to use this plugin in your documentation, simply setup a `.pages.yml` file in any subdirectory you like.

In our example do we have the following `.pages.yml` file setup inside `docs/posts/`:  
```yaml
nav:
- 'My Posts': index.md
- ... # List all pages and their subdirectories
```

Moving forward can we now add a `{nav}` placeholder inside the file where we want the navigation to be generated:  
```markdown
# My Posts
This page lists all my posts I made.  
Take a look at the nav list below.

## Posts
{nav} <!-- This will be replaced by the plugin -->
```

Let's assume we have the following folder structure:  
```yaml
docs/
├ index.md
├ assets/
│  ├ css/ # Some CSS assets
│  │  └ ...
│  └ img/ # Some images
│     └ ...
└ posts/
   ├ .pages.yml # Page navigation of awesome-pages
   ├ index.md   # This is the page with the {nav}
   ├ post1.md
   ├ post2.md
   └ archive/
      └ post3.md
```

The above would now result in `{nav}` being turned into a list equivalent to having the following Markdown:  
```markdown
- [Post1](post1.md)
- [Post2](post2.md)
- Archive
  - [Post3](archive/post3.md)
```

## Notes
I'm not the creator of this plugin. The code was provided by lukasgeiter. I only have it published here to use in some of my projects.  
Please do not ask me for support with this, as I have no real knowledge with Python in general and couldn't help solving any bugs or issues here.
