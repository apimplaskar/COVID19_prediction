from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Ridge
import pandas as pd
import numpy as np
import random

#returns sample taken from normal distribution, bounds the sample with min and max
DEFAULT_MIN = 1e-25
DEFAULT_MAX = 999999
def normal_sample (mean,sd,mn,mx,normal,rnd):
    if not normal:
        return random.randint(mn,mx)
    else:
        sample = max(mn, min(mx, np.random.normal(mean, sd)))
        if rnd:
            return int(sample)
        else:
            return sample


def MAPE(pred, valid):
    pred = pred.reset_index()
    valid = valid.reset_index()
    pred = pred.astype('int64')
    valid = valid.astype('int64')
    v = pred.subtract(valid)
    v = v.divide(valid)
    v = v.abs()
    v = v.sum(axis = 0)
    #v = v[0]+v[1]+v[2]
    n = len(pred)
    return v/n

class hyperparam_scan:
    
    def __init__(self,feature_list,gaussian_parameters,sd_scale,initial_parameters,estimator):
        self.feature_list = feature_list
        self.lowest_errors = {f+'_error':1 for f in feature_list}
        self.gaussian_parameters = gaussian_parameters
        self.sd_scale = sd_scale
        self.initial_parameters = initial_parameters
        self.best_parameters = [initial_parameters]
        self.estimator = estimator
        self.iteration = 0
        
        
    def get_reg(self):
        
        #get ridge classifier        
        parameters = {}
        for p in self.best_parameters[-1]:
            if "error" in p:
                continue
            gp = self.gaussian_parameters[p]
            parameters[p] = normal_sample(self.best_parameters[-1][p], gp['sd']*self.sd_scale, gp['mn'], gp['mx'],gp['normal'],gp['rnd'])
        passed_parameters = {p:parameters[p] for p in parameters if ("ignore" not in self.gaussian_parameters[p])}
        reg = MultiOutputRegressor(estimator=self.estimator(**passed_parameters))
        return (reg,parameters)
    
    
    def evaluate_test(self,parameters,test,validation):
        errors = MAPE(test[self.feature_list], validation[self.feature_list])
               
        for f in self.feature_list:
            parameters[f+'_error'] = errors[f]
        improvements = []
        for p in parameters:
            if "error" in p:
                if(parameters[p] < self.lowest_errors[p]):
                    self.lowest_errors[p] = parameters[p]
                    improvements.append(p)
                    
        if self.iteration == 0:
            print_str2 = ' SETUP:'
        else:
            print_str2 = ' ITERATION '+str(self.iteration)+': '
        
        if len(improvements) > 0:
            self.best_parameters.append(parameters)
            self.sd_scale *= (len(self.best_parameters) - 1) / len(self.best_parameters)
            print_str1 = '(*)'
        else:
            print_str1 = '(-)'

        print(print_str1+print_str2+str([(i,self.lowest_errors[i]) for i in improvements]))
        self.iteration += 1;
        
        
    def print_best(self):
        if len(self.best_parameters) == 1:
            print("Ititial parameters were the best. No good parameters found!")
            print(self.best_parameters[0])
            print()
            return
        for parameters in self.best_parameters[1:]:
            for p in parameters:
                if ("error" in p) and (parameters[p] <= self.lowest_errors[p]):
                    print(parameters)
                    print()
                    break
        
                    
        
        

    
    
        


        
        
        
        