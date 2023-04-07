# for permutations function
import itertools


class TopSecretAlgorithm:
    '''
    TopSecretAlgorithm Assign shipment destinations to drivers
    ...

    Attributes
    ----------
    streets : list
        Tuple list of streets (street, multiplier for SS, length)
    drivers : list
        Tuple list of drivers (driver, vowels, consonants, length)
    assignation : dictionary
        Store calculated shipments (higher SS)
    '''

    def __init__(self, streetFile, driversFile):
        '''
        Parameters
        ----------
        streetFile : str
            Filepath to streets names file
        driversFile : str
            Filepath to drivers names file
        '''

        # streets and drivers list
        self.streets = []
        self.drivers = []
        self.assignation = {
            'ss': 0,
            'shipments': []
        }

        # parse streets file
        self.__parseStreetFile(streetFile)
        # parse drivers file
        self.__parseDriverFile(driversFile)

    def assignDestinations(self):
        '''
        Calculate the highest achievable base suitability score

        '''
        # get list of permutations
        permutations = [list(zip(self.streets, p))
                        for p in itertools.permutations(self.drivers)]

        # SS values
        ssList = []

        # for each permutation
        for permList in permutations:
            # initialize SS value
            ss = 0

            # for each tuple
            for tp in permList:
                # get actual tuples
                # street tuple (street, multiplier for SS, length)
                streetTp = tp[0]
                # driver tuple (driver, vowels, consonants, length)
                driverTp = tp[1]

                # get street multiplier value
                streetMultiplier = streetTp[1]

                # get lengths of street and driver
                streetLength = streetTp[2]
                driverLength = driverTp[3]

                # if street multiplier is 1.5
                if streetMultiplier == 1.5:
                    # calculate SS with 1.5 and vowels
                    ss += streetMultiplier * driverTp[1]
                else:
                    # calculate SS with 1 and consonants
                    ss += streetMultiplier * driverTp[2]

                # if string lengths are equal
                if streetLength == driverLength:
                    # recalculate the SS value
                    ss += (ss * .5)

            # add the SS value to the list
            ssList.append(ss)

        # get index of higher ss
        maxSsIndex = ssList.index(max(ssList))

        # define the result
        self.__assignDestinations(permutations[maxSsIndex], ssList[maxSsIndex])

    def getAssignation(self):
        '''
        Return the 'assignation' field
        '''
        return self.assignation

    def __assignDestinations(self, permList, ss):
        '''
        Define and format the result in the 'assignation' field
        ...

        Parameters
        ----------
        permList : list
            List of final shipment tuples
        ss : float
            SS obtainable by shipment tuples list
        '''

        # assign the ss value
        self.assignation['ss'] = ss

        # for each tuple
        for tp in permList:
            # get actual tuples
            streetTp = tp[0]
            driverTp = tp[1]

            # define the shipment
            shipment = {
                'street': streetTp[0],
                'driver': driverTp[0]
            }

            # add actual tuple to the result
            self.assignation['shipments'].append(shipment)

    def __parseStreetFile(self, streetFile):
        '''
        Parse the streets file to a tuple form
        ...

        Parameters
        ----------
        streetFile : str
            Filepath to streets names file
        '''

        # get file lines
        lines = self.__readFileAsLines(streetFile)

        # for each line
        for line in lines:
            # get actual street
            street = line.strip()
            # get the length
            length = len(street)

            multiplier = 1
            if length % 2 == 0:
                # even length
                multiplier = 1.5

            # define tuple (street, multiplier for SS, length)
            tp = (street, multiplier, len(street))

            # add tuple to street list
            self.streets.append(tp)

    def __parseDriverFile(self, driversFile):
        '''
        Parse the driver file to a tuple form
        ...

        Parameters
        ----------
        driversFile : str
            Filepath to drivers names file
        '''
        # get file lines
        lines = self.__readFileAsLines(driversFile)

        # define vowels
        vowels = ['a', 'e', 'i', 'o', 'u', 'a', 'é', 'í', 'ó', 'ú']

        # for each line
        for line in lines:
            # get actual driver
            driver = line.strip()
            driverLC = driver.lower()

            # counters
            totalVowels = 0
            totalConsonants = 0

            for char in driverLC:
                if char in vowels:
                    totalVowels += 1
                elif char != ' ':
                    totalConsonants += 1

            # define tuple (driver, vowels, consonants, length)
            tp = (driver, totalVowels, totalConsonants, len(driver))

            # add tuple to driver list
            self.drivers.append(tp)

    def __readFileAsLines(self, file):
        '''
        Read a file by lines
        ...

        Parameters
        ----------
        file : str
            Filepath to read
        '''
        try:
            # open the file in read mode
            file = open(file, 'r', encoding='utf-8')
            lines = file.readlines()

            # close the file
            file.close()
        except:
            print('File reading error: ', file)
            exit()

        # return lines
        return lines
