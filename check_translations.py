#!/usr/bin/env python3
"""
سكريبت سريع للتحقق من نظام الترجمة
Quick script to verify translation system
"""

import sys

def check_translations():
    """التحقق من نظام الترجمة | Check translation system"""
    
    print("=" * 60)
    print("🔍 فحص نظام الترجمة | Translation System Check")
    print("=" * 60)
    print()
    
    # 1. التحقق من الملفات الأساسية
    print("1️⃣ التحقق من الملفات | Checking Files:")
    
    try:
        import i18n
        print("   ✅ i18n.py موجود | i18n.py exists")
    except ImportError:
        print("   ❌ i18n.py غير موجود | i18n.py not found")
        return False
    
    try:
        import additional_translations
        print("   ✅ additional_translations.py موجود | additional_translations.py exists")
    except ImportError:
        print("   ⚠️  additional_translations.py غير موجود | additional_translations.py not found")
    
    print()
    
    # 2. عدد الترجمات قبل الدمج
    print("2️⃣ إحصائيات الترجمة | Translation Statistics:")
    
    from i18n import MESSAGES, SUPPORTED_LANGUAGES
    
    original_count = len(MESSAGES)
    print(f"   📊 عدد المفاتيح الأصلية | Original keys: {original_count}")
    
    # 3. محاولة دمج الترجمات الإضافية
    try:
        from additional_translations import ADDITIONAL_TRANSLATIONS
        
        # Count only new keys
        new_keys = [k for k in ADDITIONAL_TRANSLATIONS.keys() if k not in MESSAGES]
        new_count = len(new_keys)
        
        # Merge
        MESSAGES.update(ADDITIONAL_TRANSLATIONS)
        total_count = len(MESSAGES)
        
        print(f"   ➕ مفاتيح إضافية جديدة | New additional keys: {new_count}")
        print(f"   📊 إجمالي المفاتيح | Total keys after merge: {total_count}")
        print()
        
        if new_count > 0:
            print(f"   ✅ تم دمج {new_count} مفتاح جديد بنجاح!")
            print(f"   ✅ Successfully merged {new_count} new keys!")
        else:
            print("   ℹ️  جميع المفاتيح الإضافية موجودة مسبقاً")
            print("   ℹ️  All additional keys already exist")
        
    except ImportError:
        print("   ⚠️  الترجمات الإضافية غير متاحة")
        print("   ⚠️  Additional translations not available")
        total_count = original_count
    
    print()
    
    # 4. اللغات المدعومة
    print("3️⃣ اللغات المدعومة | Supported Languages:")
    for lang in SUPPORTED_LANGUAGES:
        lang_name = "الإنجليزية" if lang == "en" else "العربية"
        print(f"   🌍 {lang} - {lang_name}")
    
    print()
    
    # 5. اختبار بعض الترجمات
    print("4️⃣ اختبار الترجمات | Test Translations:")
    
    test_keys = [
        "common.yes",
        "common.loading",
        "language.english",
        "language.arabic",
        "action.create",
        "action.save"
    ]
    
    from i18n import t
    
    found = 0
    missing = 0
    
    for key in test_keys:
        if key in MESSAGES:
            ar_text = MESSAGES[key].get("ar", "N/A")
            en_text = MESSAGES[key].get("en", "N/A")
            print(f"   ✅ {key}")
            print(f"      EN: {en_text}")
            print(f"      AR: {ar_text}")
            found += 1
        else:
            print(f"   ❌ {key} - غير موجود | not found")
            missing += 1
    
    print()
    
    # 6. النتيجة النهائية
    print("=" * 60)
    print("📊 النتيجة النهائية | Final Result:")
    print("=" * 60)
    print(f"✅ إجمالي المفاتيح | Total Keys: {total_count}")
    print(f"✅ اللغات المدعومة | Supported Languages: {len(SUPPORTED_LANGUAGES)}")
    print(f"✅ اختبارات ناجحة | Successful Tests: {found}/{len(test_keys)}")
    
    if missing > 0:
        print(f"⚠️  اختبارات فاشلة | Failed Tests: {missing}/{len(test_keys)}")
    
    print()
    
    # 7. عينة من الترجمات الإضافية
    try:
        from additional_translations import ADDITIONAL_TRANSLATIONS
        print("5️⃣ عينة من الترجمات الإضافية | Sample Additional Translations:")
        
        sample_keys = list(ADDITIONAL_TRANSLATIONS.keys())[:5]
        for key in sample_keys:
            ar = ADDITIONAL_TRANSLATIONS[key].get("ar", "N/A")
            en = ADDITIONAL_TRANSLATIONS[key].get("en", "N/A")
            print(f"   • {key}")
            print(f"     EN: {en}")
            print(f"     AR: {ar}")
        
        print()
        
    except ImportError:
        pass
    
    print("=" * 60)
    print("✅ تم الفحص بنجاح | Check completed successfully!")
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    try:
        success = check_translations()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ خطأ | Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
