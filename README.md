#person-names-extractor

Extract person names from texts and articles. 

### How to run

1. Build
```bash
git clone https://github.com/sobir-git/people-names-extractor
cd people-names-extractor/
docker build -t personextractor .
```

2. Run 

Interactively
```bash
docker run -it personextractor
```

Or feed url(s)
```bash
docker run -it personextractor <url>
``` 


### Examples
Interactive mode
```bash
docker run -it personextractor
>> Donald Trump had a meeting with Vladimir Putin yesterday. There were drinking vodka and visiting banya all night long. Alexander Lukashenko was offended that he was not in a party.
['Donald Trump', 'Vladimir Putin', 'Alexander Lukashenko']

>> Bezos was born Jeffrey Preston Jorgensen in Albuquerque, New Mexico, on January 12, 1964, the son of Jacklyn (née Gise) and Ted Jorgensen.
['Bezos', 'Jeffrey Preston Jorgensen', 'Jacklyn', 'Ted Jorgensen']

>> Andy Jassy, who was recently named CEO of Amazon Web Services, says the cloud computing business is just getting started and has a bright future in enterprise computing.
['Andy Jassy']
```

Scraping a url https://www.biographyonline.net/people/100-most-influential.html
```bash
docker run -it personextractor https://www.biographyonline.net/people/100-most-influential.html
['Michael H. Hart', 'Muhammad', 'Isaac Newton', 'Jesus', 'Nazareth', 'Buddha', 'Confucius', 'St. Paul', 'Ts’ai Lun', 'Johann Gutenberg', 'Christopher Columbus', 'Albert Einstein', 'Louis Pasteur', 'Aristotle', 'Euclid', 'Charles Darwin', 'Shih Huang Ti', 'Qin', 'Augustus Caesar', 'Constantine the Great', 'James Watt', 'Watt', 'Michael Faraday', 'James Clerk Maxwell', 'Martin Luther', 'George Washington', 'Karl Marx', 'Wilbur Wright Orville', 'Wilbur', 'Genghis Kahn', 'Mongols', 'Adam Smith', 'William Shakespeare', 'John Dalton', 'Alexander the Great', 'Napoleon Bonaparte', 'Thomas Edison', 'Antony van Leeuwenhoek', 'William T.G. Morton', 'Guglielmo Marconi', 'Adolf Hitler', 'Plato', 'Oliver Cromwell', 'Alexander Graham Bell', 'Alexander Fleming', 'John Locke', 'Locke', 'Ludwig van Beethoven', 'Werner Heisenberg', 'Louis Daguerre', 'Simon Bolivar', 'Rene Descartes', 'Michelangelo', 'Umar ibn al-Khattab', 'Asoka', 'William Harvey', 'Ernest Rutherford', 'John Calvin', 'Gregor Mendel', 'Max Planck', 'Joseph Lister', 'Francisco Pizarro', 'Conquistador', 'Hernando Cortes', 'Thomas Jefferson', 'Queen Isabella', 'Joseph Stalin', 'Julius Caesar', 'William the Conqueror', 'Sigmund Freud', 'Edward Jenner', 'Wilhelm Conrad Roentgen', 'Johann Sebastian Bach', 'Composer', 'Lao Tzu', 'Tao Te Ching', 'Johannes Kepler', 'mathematician', 'Enrico Fermi', 'Leonhard Euler', 'Jean-Jacques Rousseau', 'Nicoli Machiavelli', 'Thomas Malthus', 'John F. Kennedy', 'Gregory Pincus', 'Mani', 'Lenin', 'Sui Wen Ti', 'Cyrus the Great', 'Peter the Great', 'Mao Zedong', 'Francis Bacon', 'Creator', 'Henry Ford', 'Mencius', 'Zoroaster', 'Queen Elizabeth', 'Armada', 'Mikhail Gorbachev', 'Charlemagne', 'Homer Greek', 'Michael H. 1992', 'Citadel Press Book', 'Runner Ups', 'Michael Hart', 'Abraham Lincoln', 'Sri Krishna', 'The Bhagavad Gita', 'Guru Nanak', 'Pettinger', 'Tejvan', 'Newton', 'Jesus Christ', 'Queen Victoria', 'Einstein', 'Gandhi', 'Cleopatra', 'Diana', 'Marie Curie', 'Joan', 'Eleanor Roosevelt', 'Mother Teresa', 'Emil Zatopek']
```
