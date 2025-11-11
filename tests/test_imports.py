"""
Basic import tests for LisezMoiCreator
Tests that all modules can be imported without errors
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_main_import():
    """Test that main module can be imported"""
    try:
        import main
        print("✓ main module imported successfully")
        return True
    except ImportError as e:
        # PyQt6 may fail in headless environments, which is expected
        if 'libEGL' in str(e) or 'display' in str(e).lower():
            print("⚠ main module requires display server (expected in headless env)")
            return True  # This is acceptable
        else:
            print(f"✗ Failed to import main: {e}")
            return False


def test_ui_imports():
    """Test that UI modules can be imported (without Qt display)"""
    modules_to_test = [
        'ui',
        'ui.tabs',
    ]
    
    all_passed = True
    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✓ {module_name} imported successfully")
        except ImportError as e:
            # PyQt6 may fail in headless environments, which is expected
            if 'libEGL' in str(e) or 'display' in str(e).lower():
                print(f"⚠ {module_name} requires display server (expected in headless env)")
            else:
                print(f"✗ Failed to import {module_name}: {e}")
                all_passed = False
    
    return all_passed


def test_package_structure():
    """Test that package structure is correct"""
    required_files = [
        'main.py',
        'setup.py',
        'requirements.txt',
        'README.md',
        'ui/__init__.py',
        'ui/main_window.py',
        'ui/tabs/__init__.py',
        'ui/tabs/general_info_tab.py',
        'ui/tabs/prerequisites_tab.py',
        'ui/tabs/description_tab.py',
        'ui/tabs/installation_tab.py',
        'ui/tabs/uninstallation_tab.py',
        'ui/tabs/credits_tab.py',
    ]
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    all_exist = True
    
    for file_path in required_files:
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            all_exist = False
    
    return all_exist


if __name__ == '__main__':
    print("=" * 60)
    print("LisezMoiCreator - Basic Import Tests")
    print("=" * 60)
    
    print("\n1. Testing main module import...")
    test1 = test_main_import()
    
    print("\n2. Testing UI module imports...")
    test2 = test_ui_imports()
    
    print("\n3. Testing package structure...")
    test3 = test_package_structure()
    
    print("\n" + "=" * 60)
    if test1 and test2 and test3:
        print("All tests passed! ✓")
        sys.exit(0)
    else:
        print("Some tests failed. Please check the output above.")
        sys.exit(1)
