#!/usr/bin/env python
import argparse
import yaml
from glob import glob
from pykwalify.core import Core
from os.path import join


class Organization:
    def __init__(self, source):
        with open(source) as fh:
            source = yaml.load(fh)
        self.name = source["name"]
        self.website = source["website"]
        self.description = source["description"]

    def to_html(self):
        """return html"""
        return f"""
    <tr>
    <td>
      <img width="300px" src=""/>
    </td>
    <td>
       <h1>{self.name}</h1>
       <p>
        {self.description}
       </p>
       <p>
         <a href="{self.website}">Website</a>
       </p>
    </td>
  </tr>
    """


def validate(source, schema="org-schema.yaml"):
    c = Core(source_file=source, schema_files=[schema])
    c.validate(raise_exception=True)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("orgs", type=str)
    return p.parse_args()


def main():
    args = parse_args()
    orgs = [Organization(o) for o in glob(join(args.orgs, "*.yaml"))]

    html = "\n".join(o.to_html() for o in orgs)

    with open("Organizations.md", "w") as fh:
        fh.write("---")
        fh.write("title: Confirmed Organizations")
        fh.write("---")
        fh.write("<table>")
        fh.write(html)
        fh.write("</table>")


if __name__ == "__main__":
    main()
