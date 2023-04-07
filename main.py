# for args parsing
import sys
import getopt

# import custom files
from TopSecretAlgorithm import TopSecretAlgorithm


class App:
    '''
    App is the main class of the program
    '''

    def __init__(self):
        # streets and drivers files name
        self.streetsFile = ''
        self.driversFile = ''

    def run(self, argv):
        # get the args
        opts, args = getopt.getopt(argv, 'hs:d:')

        # for each arg tuple
        for opt, arg in opts:
            if opt == '-h':
                # help option
                print('Run example => main.py -s <streets_file> -d <drivers_file>')
                sys.exit()

            elif opt in ('-s', '--streets'):
                # streets file option
                self.streetsFile = arg

            elif opt in ('-d', '--drivers'):
                # drivers file option
                self.driversFile = arg

        # simple check for files names
        if not self.streetsFile or not self.driversFile:
            print('Please provide streets and drivers files name')
            exit()

        # execute TopSecretAlgorithm
        TopSA = TopSecretAlgorithm(self.streetsFile, self.driversFile)
        # generate the result
        TopSA.assignDestinations()
        # get the result
        assignations = TopSA.getAssignation()

        # show the result
        print(assignations)


# start of the app
if __name__ == '__main__':
    App = App()
    App.run(sys.argv[1:])
