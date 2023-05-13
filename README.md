# handlebars.py

Handlebars templating from the commandline. 

Make sure you install pybars first

```
pip install pybars
```

All handlebars templating magic works. 
When using a yaml file. Just add template variables like so

```
firstname: Marco
```

But Handlebars paths fully work as well.
For more information see: https://handlebarsjs.com/


## Examples

You can add a yaml file to hold all the data: 
```
printf "{{#each people}}\n{{ ../prefix}} {{first_name}}\n{{/each}}" | python3 handlebars.py -f data.yaml
```

Or just use arguments to pass the data to the template. 

```
echo -e "Hi {{name}}" | python3 handlebars.py --name Marco
# Hi Marco
echo -e "Hello {{thing}}" | python3 handlebars.py --thing World
# Hello World
```

