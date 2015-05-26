

    


    %matplotlib inline
    import networkx as nx
    import matplotlib.pyplot as plt
    import functools
    import configparser
    import re

# Calling python function


    G = nx.fast_gnp_random_graph(10, .3)
    nx.draw_networkx(G)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_3_0.png)


# Calling python function using strings
## Using `getattr()`


    G2 = getattr(nx, 'moebius_kantor_graph')()
    nx.draw_networkx(G2)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_5_0.png)



    G3 = getattr(nx, 'fast_gnp_random_graph')(15, .5)
    nx.draw_networkx(G3)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_6_0.png)


# Using a configfile


    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['Network Parameters'] = {}
    
    network_parameters = config['Network Parameters']
    network_parameters['graph with no parameters'] = 'moebius_kantor_graph'
    network_parameters['graph with parameters'] = 'fast_gnp_random_graph'
    network_parameters['num_nodes'] = '24'
    network_parameters['probability edge creation'] = '.34'
    
    with open('example.ini', 'w') as configfile:
        config.write(configfile)


    %%bash
    cat example.ini

    [Network Parameters]
    graph with no parameters = moebius_kantor_graph
    graph with parameters = fast_gnp_random_graph
    num_nodes = 24
    probability edge creation = .34
    



    config.sections()




    ['Network Parameters']



## Using `getattr()`


    g_config_no_param = getattr(nx, config.get('Network Parameters', 'graph with no parameters'))()
    nx.draw_networkx(g_config_no_param)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_12_0.png)



    g_config_param = \
        getattr(nx, config.get('Network Parameters', 'graph with parameters'))\
        (config.getint('Network Parameters', 'num_nodes'),
         config.getfloat('Network Parameters', 'probability edge creation'))
    nx.draw_networkx(g_config_param)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_13_0.png)


## Using `functools.partial()`


    def partial(func, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = keywords.copy()
            newkeywords.update(fkeywords)
            return func(*(args + fargs), **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc


    function_name = config.get('Network Parameters', 'graph with no parameters')
    graphs = partial(getattr(nx, function_name))


    g_partial = graphs()
    nx.draw_networkx(g_partial)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_17_0.png)


## Parse the config file


    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['Network Parameters'] = {}
    
    network_parameters = config['Network Parameters']
    network_parameters['graph with no parameters'] = 'moebius_kantor_graph'
    network_parameters['graph with parameters'] = 'fast_gnp_random_graph'
    network_parameters['args'] = 'int 24, float .34, str "hello world", str "goodbye"'
    network_parameters['kwargs'] = ''
    
    with open('example.ini', 'w') as configfile:
        config.write(configfile)


    %%bash
    cat example.ini

    [Network Parameters]
    graph with no parameters = moebius_kantor_graph
    graph with parameters = fast_gnp_random_graph
    args = int 24, float .34, str "hello world", str "goodbye"
    kwargs = 
    


### The parser function


    def _parse_args(str_args):
        list_args = []
        args = list(x.strip() for x in str_args.split(','))
        # print(args)
        for arg in args:
            str_type, str_value = arg.split(' ', maxsplit=1)
            str_value = re.sub('\'|\"', '', str_value)
            # print((str_type), (str_value))
            casted_variable = getattr(__builtin__, str_type)(str_value)
            # print(casted_variable)
            list_args.append(casted_variable)
        # print(list_args)
        return list_args


    def _parse_kwargs(str_kwargs):
        dict_kwargs = {}
        return dict_kwargs


    def arg_parser(str_args='', str_kwargs=''):
        list_args = _parse_args(str_args)
        dict_kwargs = _parse_kwargs(str_kwargs)
        
        return_value = list((list_args, dict_kwargs))
        print(return_value)
        return(return_value)

### Testing is good


    args = config.get('Network Parameters', 'args')
    kwargs = config.get('Network Parameters', 'kwargs')
    
    print(args)
    print(kwargs)
    
    calculated = arg_parser(args, kwargs)
    expected = [[24, .34, "hello world", 'goodbye'], {}]
    assert(calculated == expected)
    calculated

    int 24, float .34, str "hello world", str "goodbye"
    
    [[24, 0.34, 'hello world', 'goodbye'], {}]





    [[24, 0.34, 'hello world', 'goodbye'], {}]



## Pass in the parsed arguments into functools.partial()


    config = configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['Network Parameters'] = {}
    
    network_parameters = config['Network Parameters']
    network_parameters['graph with no parameters'] = 'moebius_kantor_graph'
    network_parameters['graph with parameters'] = 'fast_gnp_random_graph'
    network_parameters['args'] = 'int 24, float .34'
    network_parameters['kwargs'] = '{}'
    
    with open('example.ini', 'w') as configfile:
        config.write(configfile)


    %%bash
    cat example.ini

    [Network Parameters]
    graph with no parameters = moebius_kantor_graph
    graph with parameters = fast_gnp_random_graph
    args = int 24, float .34
    kwargs = {}
    



    function_name = config.get('Network Parameters', 'graph with parameters')
    function_args = config.get('Network Parameters', 'args')
    function_kwargs = config.get('Network Parameters', 'kwargs')
    
    function_parameters = arg_parser(function_args, function_kwargs)
    function_parameters

    [[24, 0.34], {}]





    [[24, 0.34], {}]



## Magic


    graphs = partial(getattr(nx, function_name))
    g_strings = graphs(*function_parameters[0], **function_parameters[1])
    nx.draw_networkx(g_strings)


![png](Function%20calls%20with%20strings_files/Function%20calls%20with%20strings_32_0.png)

