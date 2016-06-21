import random

import numpy
import numpy.random


#from inits
ALPHA = .7
GAMMA = .8
EPSILON = .1


NUM_EPISODES=1
CAT_CAP=round(19135/NUM_EPISODES)
CREDIT=1
DO_NOT_CREDIT=0


def get_categories(dataframe, index):
    categories_applied = dataframe.AmountCategory[index]
    return categories_applied

class Node(object):
    def __init__(self, tag, index, reward):
        self.tag = tag;
        self.transitions = [];
        self.index = index
        
    def get_reward(self):
        return self.reward
    
    def get_index(self):
        return self.index
        
    def add_transition(self, transition):
        self.transitions.append(transition)
 
    def to_string(self):
        return "%s" % self.tag
    
    def get_random_neighbor(self):
        ran = numpy.random.choice(len(self.transitions), 1)
        transition = self.transitions[ran[0]]
        return transition.get_next()
    
    def get_best_neighbor(self, Q, state_index):
        # We pick the best option using the Q value table
        
        do_not_credit_value = Q[0 * CAT_CAP + state_index]
        credit_value = Q[1 * CAT_CAP + state_index]
        
        # Quick and very dirty TODO: clean!!!
        if len(self.transitions) > 1:
            # This means we have two transitions
            if(do_not_credit_value < credit_value):
                #credit
                if self.transitions[0].get_next().get_index() == CREDIT:
                    return self.transitions[0].get_next()
                else:
                    return self.transitions[1].get_next()
            else:
                #do not credit
                if self.transitions[0].get_next().get_index() == DO_NOT_CREDIT:
                    return self.transitions[0].get_next()
                else:
                    return self.transitions[1].get_next()
        else:
            return self.transitions[0].get_next()

    def say_hi(self):
        print self.tag

class Transition():
    def __init__(self, to_node):
        self.to_node = to_node
    
    def to_string(self):
        return "   --[s%]--> %s" % (self.weight, self.to_node.to_string())
    
    def get_next(self):
        return self.to_node
    
class State(Node):
    '''
    Inherits from Node, it holds a reward to reach this state.
    '''
    def __init__(self, tag, index, reward=0):
        super(State, self).__init__(tag, index, reward)
    def say_hi(self):
        print "state: %s" % self.tag
        
    def view_world(self):
        
        pass
    
    def get_reward(self):
        categories = get_categories(df_data2, index_person)
        print "The person is applying for %s levels of amount" % categories
        return categories * 500
            
class Action(Node):
    '''
    Inherits from Node, this type of node just represents an action, there is no
    reward.
    '''
    def __init__(self, tag, index, reward=0):
        super(Action, self).__init__(tag, index, reward)
    def say_hi(self):
        print "action: %s" % self.tag
    
    def act_on_world(self):
        if self.index == CREDIT:
            credit_something(df_data2)
    
    def get_reward(self):
        if self.index == CREDIT:
            return -1
        else:
            return 0
        
        
        
        
        
        
        
        
class Graph():
    '''
    The graph object starts with an initial node, this node will have a set
    of transitions, that lead to other nodes. Current node is a pointer that 
    points to the actual state.
    '''
    def __init__(self, initial_node):
        self.initial_node = initial_node
        self.nodes = []
        self.add_node(initial_node)
        self.current_node = initial_node
        
    def add_node(self, node):
        self.nodes.append(node)
        
    def get_current(self):
        return self.current_node
    
    def step(self, EPSILON, Q):
        
        if(random.random() < EPSILON):
            # we chose random next step
            print 'Epsilon decision'
            self.current_node.view_world()
            return self.current_node.get_random_neighbor()
            
        else:
            # we choose the next action using the Q table
            print 'Q decision'
            self.current_node.view_world()
            return self.current_node.get_best_neighbor(Q, self.current_node.get_index())
    
    def moveToNode(self, nextStep):
        self.current_node = nextStep
    
    def simple_step(self):
        self.current_node.act_on_world()
        return self.current_node.get_random_neighbor()
        
        
    
    
        
        
        
        