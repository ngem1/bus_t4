import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ADDRESS, CONF_ID, CONF_UPDATE_INTERVAL, CONF_USE_ADDRESS

# Avoid importing the whole cover module directly
from esphome.components import cover as cover_ns

bus_t4_ns = cg.esphome_ns.namespace('bus_t4')
Nice = bus_t4_ns.class_('NiceBusT4', cover_ns.Cover, cg.Component)

# Debugging prints
print("Debug: Namespace and NiceBusT4 class created successfully")

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Nice),
    cv.Optional(CONF_ADDRESS): cv.hex_uint16_t,
    cv.Optional(CONF_USE_ADDRESS): cv.hex_uint16_t,
}).extend(cv.COMPONENT_SCHEMA).extend(cover_ns.COVER_SCHEMA)

def to_code(config):
    print("Debug: Running to_code function")
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield cover_ns.register_cover(var, config)

    if CONF_ADDRESS in config:
        cg.add(var.set_to_address(config[CONF_ADDRESS]))
        print(f"Debug: Address set to {config[CONF_ADDRESS]}")

    if CONF_USE_ADDRESS in config:
        cg.add(var.set_from_address(config[CONF_USE_ADDRESS]))
        print(f"Debug: Use address set to {config[CONF_USE_ADDRESS]}")
