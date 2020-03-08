# To help with testing
Create a file on your Pc called Enigma-master
In it, create two folders, "code" and "test"
In "code", put only encrypt.py and decrypt.py so you can edit them
In "test", put both .py files and all three .txt files.
That wat, when you make changes, you can just copy the files over.
When copying, to make it easier, you can do this in your home directory:

## Windows
Go to Enigma-master
Create a file, "test.bat", and in it put the following code:
	xcopy code test
When asked with the interface, press a, as you want to override the old versions that are in the "test" directory with the new modifications from the "code" directory

## Linux
Same as above, only except for "test.bat" you make "test.sh" and put:
	rsync -r code/ test
That way only what you've changed will be copied, no need for user input

## MacOSX
Afaik, you have to do:
	cp ~/Whatever/Enigma-master/code ~/Whatever/Enigma-master/test
Please feel free to update this, as I couldn't find anything on the Internet, and I don't have a Mac, I have Windows.