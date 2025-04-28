import pytest


# @pytest.mark.parametrize("input,expected",[
#     ("A","a"),
#     ("B","b"),
#     ("C","C")])
# def test_params(input,expected):
#     print("Actual ---> "+input)
#     print("Expected ---> "+expected)
#     assert input.lower() == expected


@pytest.mark.order(1)
def test_run_with_order_a():
    print("Method 1")



@pytest.mark.order(3)
def test_run_with_order_c(): 
    print("Method 3")


@pytest.mark.order(2)
def test_run_with_order_b():   
    print("Method 2")   


@pytest.mark.order(4)
def test_run_with_order_d():  
    print("Method 4")  

@pytest.mark.high()
def test_run_with_high_priority():  
    print("High Priority")     


@pytest.mark.flaky(reruns=2,reruns_delay=2)
def test_retry_case():  
    print("Retry case")
    assert True 