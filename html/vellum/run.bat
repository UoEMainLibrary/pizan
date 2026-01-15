@echo off
java -Xmx512m -classpath vv.jar VirtualVellum -dataset images.xml -threads 2 -languagefile "languages.xml"
