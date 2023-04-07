# SDE Code Exercise - Platform Science Code Exercise


# Installation

Requires [Python](https://www.python.org/downloads/) 3.11.0+ to run.
Download and execute 'python main.py'

## Create files and folders

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

## Usage
**Parameters**
- -h: show run command example
	- >Run example => main.py -s <streets_file> -d <drivers_file>
- -s: file name to streets file
- -d: file name to drivers file

## Output
The output is a python dictionary with two properties
- -SS: base suitability score
- -shipments: list of tuple with **street** and **driver** names

**Example**
```
{
	'ss': 18.0,
	'shipments': [
		{'street':  'Street ABCDE', 'driver':  'Mike Cooper'},
		{'street':  'Angel Avenue', 'driver':  'Bob Locker'},
		{'street':  'Stars Street', 'driver':  'Raúl López'}
	]
}
```