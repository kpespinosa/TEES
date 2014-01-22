import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/..")
from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn.externals import joblib

def train(examplesPath, cparameter, modelPath):
    clf = svm.SVC(gamma=0.001, C=float(cparameter))
    X_train, y_train = load_svmlight_file(examplesPath)
    print X_train
    print y_train
    clf.fit(X_train, y_train)
    joblib.dump(clf, os.path.join(modelPath, "sklearn-SVM-model.pkl")) 

if __name__=="__main__":
    # Import Psyco if available
    try:
        import psyco
        psyco.full()
        print >> sys.stderr, "Found Psyco, using"
    except ImportError:
        print >> sys.stderr, "Psyco not installed"

    from optparse import OptionParser
    optparser = OptionParser(description="Interface to scikit-learn SVM")
    optparser.add_option("-e", "--examples", default=None, dest="examples", help="Example File", metavar="FILE")
    optparser.add_option("--train", default=False, action="store_true", dest="train")
    optparser.add_option("--classify", default=False, action="store_true", dest="classify")
    optparser.add_option("-m", "--model", default=None, dest="model", help="path to model file")
    optparser.add_option("--predictions", default=None, dest="predictions", help="Predictions file")
    optparser.add_option("-c", "--cparameter", default=None, dest="cparameter", help="C-parameter")
    (options, args) = optparser.parse_args()
    
    assert options.train != options.classify
    if options.train:
        train(options.examples, options.cparameter, options.model)