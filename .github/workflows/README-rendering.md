# Cookiecutter and GH Workflows

You may ask - why do we have to split the workflow files into multiple files? How does it end up working?

Let us answer the latter part first: the addition files are "echoed" into the yaml without the `-addition*` addendum
in the [post_gen_project.sh](../../../hooks/post_gen_project.sh) hook and deleted afterwards.

Now why do we have to go through this horrible mess? The problem is that Jinja templating with the double curly braces
{{ }} as used by cookiecutter collides with github workflow variables, e.g. {{ secrets.MY_KEY }}. 
Cookiecutter then thinks it should do 
something with such expressions and throws an error. Unfortunately, there seems to be no way of letting cookiecutter
omit selected lines from templating, it can only ignore entire files (by registering the letter in the 
`_copy_without_render` section of [cookiecutter.json](../../../cookiecutter.json)). Splitting the workflows into
multiple parts, excluding some of these parts from rendering and reassembling them with a post-gen hook was the only
way I (Mischa) found to make cookiecutter and GH workflows work.

I am truly sorry... If the reader finds a solution that is at least a little less ugly, please let me know!
This readme will also be removed by the post-gen hook.
