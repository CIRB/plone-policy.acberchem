from setuptools import setup, find_packages

version = '1.1.dev0'

setup(name='policy.acberchem',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          'collective.anysurfer',
          'collective.quickupload',
          'collective.checktranslated',
          'collective.easyslider',
          'collective.galleriffic',
          'collective.portlet.videoanysurfer',
          'collective.videoanysurfer',
          'collective.stomach',
          # -*- Extra requirements: -*-
          'plonetheme.acberchem',
          'Products.PloneFormGen',
          'Solgema.fullcalendar',
          'webcouturier.dropdownmenu',
          'cirb.footersitemap',
      ],
      extras_require={
        'test': [
            'plone.app.robotframework',
        ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
