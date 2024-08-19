# synth_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def in_type(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'connected', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.in_type: got unexpected plan from when clause 1"
            with engine.prove('synthesizer', 'output_type', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.in_type: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def three_inputs(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.three_inputs: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.three_inputs: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'input_type', context,
                                  (rule.pattern(0),
                                   rule.pattern(5),
                                   rule.pattern(6),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "synth.three_inputs: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def two_inputs(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.two_inputs: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.two_inputs: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def param_s(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'output_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.param_s: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def param_c(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'output_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.param_c: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def control_out(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.control_out: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def signal_out(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.signal_out: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cos: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def phasor(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.phasor: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def noise(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.noise: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss8(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss9(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss10(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss13(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss14(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('synth')
  
  bc_rule.bc_rule('in_type', This_rule_base, 'input_type',
                  in_type, None,
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('type'),),
                  (),
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('connected_module'),
                   contexts.variable('type'),))
  
  bc_rule.bc_rule('three_inputs', This_rule_base, 'three_inputs',
                  three_inputs, None,
                  (contexts.variable('index'),
                   contexts.variable('type1'),
                   contexts.variable('type2'),
                   contexts.variable('type3'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),
                   pattern.pattern_literal(3),
                   contexts.variable('type3'),))
  
  bc_rule.bc_rule('two_inputs', This_rule_base, 'input_types',
                  two_inputs, None,
                  (contexts.variable('current_module'),
                   contexts.variable('type1'),
                   contexts.variable('type2'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),))
  
  bc_rule.bc_rule('param_s', This_rule_base, 'output_type',
                  param_s, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('param_c', This_rule_base, 'output_type',
                  param_c, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('control_out', This_rule_base, 'output_type',
                  control_out, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('id'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('signal_out', This_rule_base, 'output_type',
                  signal_out, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('id'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc0', This_rule_base, 'pd_object',
                  cc0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc0', This_rule_base, 'pd_object',
                  sc0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs0', This_rule_base, 'pd_object',
                  cs0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss0', This_rule_base, 'pd_object',
                  ss0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc1', This_rule_base, 'pd_object',
                  cc1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc1', This_rule_base, 'pd_object',
                  sc1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs1', This_rule_base, 'pd_object',
                  cs1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss1', This_rule_base, 'pd_object',
                  ss1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc2', This_rule_base, 'pd_object',
                  cc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc2', This_rule_base, 'pd_object',
                  sc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs2', This_rule_base, 'pd_object',
                  cs2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss2', This_rule_base, 'pd_object',
                  ss2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc3', This_rule_base, 'pd_object',
                  cc3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc3', This_rule_base, 'pd_object',
                  sc3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs3', This_rule_base, 'pd_object',
                  cs3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss3', This_rule_base, 'pd_object',
                  ss3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc4', This_rule_base, 'pd_object',
                  cc4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc4', This_rule_base, 'pd_object',
                  sc4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs4', This_rule_base, 'pd_object',
                  cs4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss4', This_rule_base, 'pd_object',
                  ss4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cos', This_rule_base, 'pd_object',
                  cos, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('cos~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(5),))
  
  bc_rule.bc_rule('phasor', This_rule_base, 'pd_object',
                  phasor, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('phasor~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(6),))
  
  bc_rule.bc_rule('noise', This_rule_base, 'pd_object',
                  noise, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('noise~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(7),))
  
  bc_rule.bc_rule('cc8', This_rule_base, 'pd_object',
                  cc8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc8', This_rule_base, 'pd_object',
                  sc8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs8', This_rule_base, 'pd_object',
                  cs8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss8', This_rule_base, 'pd_object',
                  ss8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc9', This_rule_base, 'pd_object',
                  cc9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc9', This_rule_base, 'pd_object',
                  sc9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs9', This_rule_base, 'pd_object',
                  cs9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss9', This_rule_base, 'pd_object',
                  ss9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc10', This_rule_base, 'pd_object',
                  cc10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc10', This_rule_base, 'pd_object',
                  sc10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs10', This_rule_base, 'pd_object',
                  cs10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss10', This_rule_base, 'pd_object',
                  ss10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc11', This_rule_base, 'pd_object',
                  cc11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc11', This_rule_base, 'pd_object',
                  sc11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs11', This_rule_base, 'pd_object',
                  cs11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss11', This_rule_base, 'pd_object',
                  ss11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc12', This_rule_base, 'pd_object',
                  cc12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc12', This_rule_base, 'pd_object',
                  sc12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs12', This_rule_base, 'pd_object',
                  cs12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss12', This_rule_base, 'pd_object',
                  ss12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc13', This_rule_base, 'pd_object',
                  cc13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc13', This_rule_base, 'pd_object',
                  sc13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs13', This_rule_base, 'pd_object',
                  cs13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss13', This_rule_base, 'pd_object',
                  ss13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc14', This_rule_base, 'pd_object',
                  cc14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc14', This_rule_base, 'pd_object',
                  sc14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs14', This_rule_base, 'pd_object',
                  cs14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss14', This_rule_base, 'pd_object',
                  ss14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('s'),))


Krb_filename = '..\\synth.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 27), (6, 6)),
    ((28, 34), (7, 7)),
    ((47, 51), (10, 10)),
    ((53, 60), (12, 12)),
    ((61, 68), (13, 13)),
    ((69, 76), (14, 14)),
    ((89, 93), (17, 17)),
    ((95, 102), (19, 19)),
    ((103, 110), (20, 20)),
    ((123, 127), (23, 23)),
    ((129, 135), (25, 25)),
    ((148, 152), (28, 28)),
    ((154, 160), (30, 30)),
    ((173, 177), (33, 33)),
    ((179, 186), (35, 35)),
    ((199, 203), (38, 38)),
    ((205, 212), (40, 40)),
    ((225, 229), (43, 43)),
    ((231, 237), (45, 45)),
    ((238, 245), (46, 46)),
    ((258, 262), (49, 49)),
    ((264, 270), (51, 51)),
    ((271, 278), (52, 52)),
    ((291, 295), (55, 55)),
    ((297, 303), (57, 57)),
    ((304, 311), (58, 58)),
    ((324, 328), (61, 61)),
    ((330, 336), (63, 63)),
    ((337, 344), (64, 64)),
    ((357, 361), (67, 67)),
    ((363, 369), (69, 69)),
    ((370, 377), (70, 70)),
    ((390, 394), (73, 73)),
    ((396, 402), (75, 75)),
    ((403, 410), (76, 76)),
    ((423, 427), (79, 79)),
    ((429, 435), (81, 81)),
    ((436, 443), (82, 82)),
    ((456, 460), (85, 85)),
    ((462, 468), (87, 87)),
    ((469, 476), (88, 88)),
    ((489, 493), (91, 91)),
    ((495, 501), (93, 93)),
    ((502, 509), (94, 94)),
    ((522, 526), (97, 97)),
    ((528, 534), (99, 99)),
    ((535, 542), (100, 100)),
    ((555, 559), (103, 103)),
    ((561, 567), (105, 105)),
    ((568, 575), (106, 106)),
    ((588, 592), (109, 109)),
    ((594, 600), (111, 111)),
    ((601, 608), (112, 112)),
    ((621, 625), (115, 115)),
    ((627, 633), (117, 117)),
    ((634, 641), (118, 118)),
    ((654, 658), (121, 121)),
    ((660, 666), (123, 123)),
    ((667, 674), (124, 124)),
    ((687, 691), (127, 127)),
    ((693, 699), (129, 129)),
    ((700, 707), (130, 130)),
    ((720, 724), (133, 133)),
    ((726, 732), (135, 135)),
    ((733, 740), (136, 136)),
    ((753, 757), (139, 139)),
    ((759, 765), (141, 141)),
    ((766, 773), (142, 142)),
    ((786, 790), (145, 145)),
    ((792, 798), (147, 147)),
    ((799, 806), (148, 148)),
    ((819, 823), (151, 151)),
    ((825, 831), (153, 153)),
    ((832, 839), (154, 154)),
    ((852, 856), (157, 157)),
    ((858, 864), (159, 159)),
    ((865, 872), (160, 160)),
    ((885, 889), (163, 163)),
    ((891, 897), (165, 165)),
    ((910, 914), (168, 168)),
    ((916, 922), (170, 170)),
    ((935, 939), (173, 173)),
    ((941, 947), (175, 175)),
    ((960, 964), (178, 178)),
    ((966, 972), (180, 180)),
    ((973, 980), (181, 181)),
    ((993, 997), (184, 184)),
    ((999, 1005), (186, 186)),
    ((1006, 1013), (187, 187)),
    ((1026, 1030), (190, 190)),
    ((1032, 1038), (192, 192)),
    ((1039, 1046), (193, 193)),
    ((1059, 1063), (196, 196)),
    ((1065, 1071), (198, 198)),
    ((1072, 1079), (199, 199)),
    ((1092, 1096), (202, 202)),
    ((1098, 1104), (204, 204)),
    ((1105, 1112), (205, 205)),
    ((1125, 1129), (208, 208)),
    ((1131, 1137), (210, 210)),
    ((1138, 1145), (211, 211)),
    ((1158, 1162), (214, 214)),
    ((1164, 1170), (216, 216)),
    ((1171, 1178), (217, 217)),
    ((1191, 1195), (220, 220)),
    ((1197, 1203), (222, 222)),
    ((1204, 1211), (223, 223)),
    ((1224, 1228), (226, 226)),
    ((1230, 1236), (228, 228)),
    ((1237, 1244), (229, 229)),
    ((1257, 1261), (232, 232)),
    ((1263, 1269), (234, 234)),
    ((1270, 1277), (235, 235)),
    ((1290, 1294), (238, 238)),
    ((1296, 1302), (240, 240)),
    ((1303, 1310), (241, 241)),
    ((1323, 1327), (244, 244)),
    ((1329, 1335), (246, 246)),
    ((1336, 1343), (247, 247)),
    ((1356, 1360), (250, 250)),
    ((1362, 1368), (252, 252)),
    ((1369, 1376), (253, 253)),
    ((1389, 1393), (256, 256)),
    ((1395, 1401), (258, 258)),
    ((1402, 1409), (259, 259)),
    ((1422, 1426), (262, 262)),
    ((1428, 1434), (264, 264)),
    ((1435, 1442), (265, 265)),
    ((1455, 1459), (268, 268)),
    ((1461, 1467), (270, 270)),
    ((1468, 1475), (271, 271)),
    ((1488, 1492), (274, 274)),
    ((1494, 1500), (276, 276)),
    ((1501, 1508), (277, 277)),
    ((1521, 1525), (280, 280)),
    ((1527, 1533), (282, 282)),
    ((1534, 1541), (283, 283)),
    ((1554, 1558), (286, 286)),
    ((1560, 1566), (288, 288)),
    ((1567, 1574), (289, 289)),
    ((1587, 1591), (292, 292)),
    ((1593, 1599), (294, 294)),
    ((1600, 1607), (295, 295)),
    ((1620, 1624), (298, 298)),
    ((1626, 1632), (300, 300)),
    ((1633, 1640), (301, 301)),
    ((1653, 1657), (304, 304)),
    ((1659, 1665), (306, 306)),
    ((1666, 1673), (307, 307)),
    ((1686, 1690), (310, 310)),
    ((1692, 1698), (312, 312)),
    ((1699, 1706), (313, 313)),
    ((1719, 1723), (316, 316)),
    ((1725, 1731), (318, 318)),
    ((1732, 1739), (319, 319)),
    ((1752, 1756), (322, 322)),
    ((1758, 1764), (324, 324)),
    ((1765, 1772), (325, 325)),
    ((1785, 1789), (328, 328)),
    ((1791, 1797), (330, 330)),
    ((1798, 1805), (331, 331)),
    ((1818, 1822), (334, 334)),
    ((1824, 1830), (336, 336)),
    ((1831, 1838), (337, 337)),
    ((1851, 1855), (340, 340)),
    ((1857, 1863), (342, 342)),
    ((1864, 1871), (343, 343)),
)
