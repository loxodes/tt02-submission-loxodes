import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
   
    dut.enable.value = 0
    dut.delay.value = 3


    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0

    await ClockCycles(dut.clk, 200)

    dut._log.info("enable")
    dut.enable.value = 1
    await ClockCycles(dut.clk, 200)
    
    dut._log.info("disable")
    dut.enable.value = 0
    await ClockCycles(dut.clk, 200)

    dut._log.info("enable then disable")
    dut.enable.value = 1
    await ClockCycles(dut.clk, 50)
    dut.enable.value = 0
    await ClockCycles(dut.clk, 100)

    dut._log.info("enable with reset")
    dut.enable.value = 1
    await ClockCycles(dut.clk, 50)
    dut.rst.value = 1
    await ClockCycles(dut.clk, 50)
