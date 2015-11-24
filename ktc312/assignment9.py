__author__ = 'ktc312'



def main():





if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Invalid inputs'
    except KeyboardInterrupt:
        print 'Quiting'
    except EOFError:
        print 'Quiting'