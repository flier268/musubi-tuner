"""
Utility functions for parsing prompt lines and command-line style arguments.
Common functions used across different generation and training scripts.
"""

import re
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


def parse_prompt_line(line: str, field_mapping: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Parse a prompt line into a dictionary of argument overrides
    
    This function parses lines in the format:
    "prompt text --w 512 --h 768 --s 30 --g 7.5"
    
    Args:
        line: Prompt line with options
        field_mapping: Optional mapping of short options to field names.
                      If None, uses default mappings for video generation.
    
    Returns:
        Dict[str, Any]: Dictionary of parsed arguments
    """
    if field_mapping is None:
        field_mapping = {
            'w': 'width',
            'h': 'height', 
            'f': 'frame_count',
            'd': 'seed',
            's': 'sample_steps',
            'g': 'guidance_scale',
            'fs': 'discrete_flow_shift',
            'l': 'cfg_scale',
            'n': 'negative_prompt',
            'i': 'image_path',
            'ei': 'end_image_path',
            'cn': 'control_video_path',
            'ci': 'control_image_path',
            'of': 'one_frame'
        }
    
    # Split on " --" to separate prompt from arguments
    parts = line.split(" --")
    prompt_dict = {"prompt": parts[0].strip()}
    
    # Initialize list fields that can have multiple values
    list_fields = {'control_image_path', 'control_image_mask_path'}
    for field in list_fields:
        if field in field_mapping.values():
            prompt_dict[field] = []
    
    # Process each argument part
    for part in parts[1:]:
        if not part.strip():
            continue
            
        try:
            # Try different parsing patterns
            
            # Pattern: "w 512" (option with integer value)
            m = re.match(r"(\w+) (\d+)", part, re.IGNORECASE)
            if m:
                option, value = m.groups()
                if option in field_mapping:
                    field_name = field_mapping[option]
                    if option == 's':  # special handling for steps
                        prompt_dict[field_name] = max(1, min(1000, int(value)))
                    else:
                        prompt_dict[field_name] = int(value)
                continue
            
            # Pattern: "g 7.5" (option with float value)
            m = re.match(r"(\w+) ([\d\.]+)", part, re.IGNORECASE)
            if m:
                option, value = m.groups()
                if option in field_mapping:
                    field_name = field_mapping[option]
                    prompt_dict[field_name] = float(value)
                continue
            
            # Pattern: "n negative prompt text" (option with string value)
            m = re.match(r"(\w+) (.+)", part, re.IGNORECASE)
            if m:
                option, value = m.groups()
                if option in field_mapping:
                    field_name = field_mapping[option]
                    # Handle list fields (can have multiple values)
                    if field_name in list_fields:
                        if field_name not in prompt_dict:
                            prompt_dict[field_name] = []
                        prompt_dict[field_name].append(value)
                    else:
                        prompt_dict[field_name] = value
                continue
                
        except ValueError as ex:
            logger.error(f"Exception in parsing argument: {part}")
            logger.error(ex)
    
    return prompt_dict


def parse_wan_prompt_line(line: str) -> Dict[str, Any]:
    """Parse a prompt line for WAN video generation with WAN-specific field mappings"""
    field_mapping = {
        'w': 'video_size_width',
        'h': 'video_size_height',
        'f': 'video_length',
        'd': 'seed',
        's': 'infer_steps',
        'g': 'guidance_scale',
        'l': 'guidance_scale',  # alternative for guidance_scale
        'fs': 'flow_shift',
        'n': 'negative_prompt',
        'i': 'image_path',
        'ei': 'end_image_path',
        'cn': 'control_path',
        'ci': 'control_image_path',
        'cim': 'control_image_mask_path',
        'of': 'one_frame_inference'
    }
    
    result = parse_prompt_line(line, field_mapping)
    
    # Clean up empty lists for control paths
    if 'control_image_path' in result and not result['control_image_path']:
        del result['control_image_path']
    if 'control_image_mask_path' in result and not result['control_image_mask_path']:
        del result['control_image_mask_path']
    
    return result


def parse_hv_prompt_line(line: str) -> Dict[str, Any]:
    """Parse a prompt line for HunyuanVideo training with HV-specific field mappings"""
    field_mapping = {
        'w': 'width',
        'h': 'height', 
        'f': 'frame_count',
        'd': 'seed',
        's': 'sample_steps',
        'g': 'guidance_scale',
        'fs': 'discrete_flow_shift',
        'l': 'cfg_scale',
        'n': 'negative_prompt',
        'i': 'image_path',
        'ei': 'end_image_path',
        'cn': 'control_video_path',
        'ci': 'control_image_path',
        'of': 'one_frame'
    }
    
    result = parse_prompt_line(line, field_mapping)
    
    # Special handling for sample_steps to apply min/max constraints
    if 'sample_steps' in result:
        result['sample_steps'] = max(1, min(1000, result['sample_steps']))
    
    return result