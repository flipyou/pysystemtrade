
from sysproduction.run_process import processToRun
from sysproduction.update_fx_prices import updateFxPrices
from sysproduction.update_sampled_contracts import updateSampledContracts
from sysproduction.update_historical_prices import updateHistoricalPrices
from sysproduction.update_multiple_adjusted_prices import updateMultipleAdjustedPrices

from sysproduction.data.get_data import dataBlob

def run_daily_price_updates():
    process_name = "run_daily_prices_updates"
    data = dataBlob(log_name=process_name)
    list_of_timer_names_and_functions = get_list_of_timer_functions_for_price_update()
    price_process = processToRun(process_name, data, list_of_timer_names_and_functions)
    price_process.main_loop()

def get_list_of_timer_functions_for_price_update():
    data_fx = dataBlob(log_name='fx_prices')
    data_contracts = dataBlob(log_name='sampled_contracts')
    data_historical = dataBlob(log_name = 'historical_prices')
    data_multiple = dataBlob(log_name = 'multiple_adj_prices')

    fx_update_object = updateFxPrices(data_fx)
    contracts_update_object = updateSampledContracts(data_contracts)
    historical_update_object = updateHistoricalPrices(data_historical)
    multiple_update_object = updateMultipleAdjustedPrices(data_multiple)

    list_of_timer_names_and_functions = [
                        ('fx_prices', fx_update_object.update_fx_prices),
        ('sampled_contracts', contracts_update_object.update_sampled_contracts),
        ('historical_prices', historical_update_object.update_historical_prices),
        ('multiple_adj_prices', multiple_update_object.update_multiple_adjusted_prices)]

    return list_of_timer_names_and_functions

